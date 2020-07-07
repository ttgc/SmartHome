using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Edge.DTO
{
    public class StatDTO
    {
        public string year { get; set; }
        public double average { get; set; }
        public double std_deviation { get; set; }
        public double heat_duration { get; set; }
        public double clim_duration { get; set; }
        public char temperature_unit { get; set; }
    }
}
