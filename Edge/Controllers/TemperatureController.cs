using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Edge.Database;

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
    }
}
