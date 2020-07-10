using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Edge.Database.Models;
using Edge.DTO;
using Edge.Utils.Conversion;

namespace Edge.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SettingsController : ControllerBase
    {
        private readonly Context context;

        public SettingsController(Context context)
        {
            this.context = context;
        }

        [HttpGet]
        public IActionResult Get()
        {
            Settings settings = context.Settings.First();
            return Ok(new SettingsDTO() { 
                house_name = settings.HouseName, clim_on = settings.ClimOn.Value,
                clim_off = settings.ClimOff.Value, heat_on = settings.HeatOn.Value,
                heat_off = settings.HeatOff.Value, temperature_unit = settings.TempUnit.Value
            });
        }

        [HttpPost]
        public IActionResult Post([FromBody] SettingsDTO body)
        {
            Settings settings = context.Settings.First();
            if (body.temperature_unit != null)
            {
                if (context.Unitstemperature.Find(body.temperature_unit) == null) return StatusCode(400);

                IDoubleConverter converter = null;
                if (settings.TempUnit.Value == 'C' || settings.TempUnit.Value == 'F')
                {
                    if (settings.TempUnit.Value == 'C' && body.temperature_unit.Value == 'F')
                    {
                        converter = new CelsiusToFahrenheit();
                        settings.TempUnit = 'F';
                    }
                    else if (settings.TempUnit.Value == 'F' && body.temperature_unit.Value == 'C')
                    {
                        converter = new FahrenheitToCelsius();
                        settings.TempUnit = 'C';
                    }
                }
                else
                {
                    return StatusCode(400);
                }
                if (converter != null)
                {
                    foreach (var t in context.Temperature)
                    {
                        t.Val = converter.Convert(t.Val);
                    }
                    settings.ClimOn = converter.Convert(settings.ClimOn.Value);
                    settings.ClimOff = converter.Convert(settings.ClimOff.Value);
                    settings.HeatOn = converter.Convert(settings.HeatOn.Value);
                    settings.HeatOff = converter.Convert(settings.HeatOff.Value);
                    context.SaveChanges();
                }
            }

            if (!String.IsNullOrEmpty(body.house_name)) settings.HouseName = body.house_name;
            if (body.clim_on != null) settings.ClimOn = body.clim_on;
            if (body.clim_off != null) settings.ClimOff = body.clim_off;
            if (body.heat_on != null) settings.HeatOn = body.heat_on;
            if (body.heat_off != null) settings.HeatOff = body.heat_off;
            context.SaveChanges();

            return Ok();
        }
    }
}
