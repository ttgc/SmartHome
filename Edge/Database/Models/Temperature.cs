using System;
using System.Collections.Generic;

namespace Edge.Database.Models
{
    public partial class Temperature
    {
        public DateTime Timer { get; set; }
        public double Val { get; set; }
    }
}
