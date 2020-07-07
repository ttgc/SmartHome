using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Edge.Database.Models;
using Edge.DTO;

namespace Edge.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TemperatureController : ControllerBase
    {
        private readonly Context context;

        public TemperatureController(Context context)
        {
            this.context = context;
        }

        [HttpGet]
        public IActionResult Get()
        {
            return StatusCode(404);
        }

        [HttpPost("{value}")]
        public IActionResult Post(double value)
        {
            IQueryable<Temperature> temperatures = context.Temperature.OrderBy(s => s.Timer);
            Temperature previous = temperatures.Count() > 0 ? temperatures.Last() : null;
            if (previous == null)
            {
                previous = new Temperature() { 
                    Timer = DateTime.MinValue, ClimOn = false, HeatOn = false 
                }; 
            }

            Settings settings = context.Settings.First();
            PostTemperatureOutputDTO dto = new PostTemperatureOutputDTO() { 
                clim_on = value >= settings.ClimOn || (previous.ClimOn.Value && value >= settings.ClimOff),
                heat_on = value <= settings.HeatOn || (previous.HeatOn.Value && value <= settings.HeatOff)
            };

            context.Temperature.Add(new Temperature() { 
                Timer = DateTime.Now, Val = value, ClimOn = dto.clim_on, HeatOn = dto.heat_on
            });
            context.SaveChanges();


            Stattemperature stats = context.Stattemperature.Find(DateTime.Now.ToString("yyyy"));
            if (stats == null)
            {
                stats = new Stattemperature() { 
                    Statyear = DateTime.Now.ToString("yyyy"), 
                    ClimDuration = new TimeSpan(), 
                    HeatDuration = new TimeSpan()
                };
                context.Add(stats);
            }
            IQueryable<Temperature> query = context.Temperature.Where(s => s.Timer.Year == DateTime.Now.Year);
            stats.Average = query.Average(s => s.Val);
            stats.StdDeviation = query.Sum(s => s.Val - stats.Average) / query.Count();
            if (previous.HeatOn.Value) stats.HeatDuration += (DateTime.Now - previous.Timer);
            if (previous.ClimOn.Value) stats.ClimDuration += (DateTime.Now - previous.Timer);
            context.SaveChanges();

            return Ok(dto);
        }
    }
}
