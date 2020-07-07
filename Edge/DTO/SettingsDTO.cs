using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Edge.DTO
{
    public class SettingsDTO
    {
        public string house_name { get; set; }
        public double? clim_on { get; set; }
        public double? clim_off { get; set; }
        public double? heat_on { get; set; }
        public double? heat_off { get; set; }
        public char? temperature_unit { get; set; }
    }
}
