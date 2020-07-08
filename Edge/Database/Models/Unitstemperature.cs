using System;
using System.Collections.Generic;

namespace Edge.Database.Models
{
    public partial class Unitstemperature
    {
        public Unitstemperature()
        {
            Settings = new HashSet<Settings>();
        }

        public char Code { get; set; }
        public string Nom { get; set; }

        public virtual ICollection<Settings> Settings { get; set; }
    }
}
