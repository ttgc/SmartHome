using System;
using System.Collections.Generic;

namespace Edge.Database.Models
{
    public partial class Stattemperature
    {
        public string Statyear { get; set; }
        public TimeSpan ClimDuration { get; set; }
        public TimeSpan HeatDuration { get; set; }
        public double Average { get; set; }
        public double StdDeviation { get; set; }
    }
}
