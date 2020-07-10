using System;
using System.Collections.Generic;

namespace Edge.Database.Models
{
    public partial class Settings
    {
        public string HouseName { get; set; }
        public double? ClimOn { get; set; }
        public double? ClimOff { get; set; }
        public double? HeatOn { get; set; }
        public double? HeatOff { get; set; }
        public char? TempUnit { get; set; }

        public virtual Unitstemperature TempUnitNavigation { get; set; }
    }
}
