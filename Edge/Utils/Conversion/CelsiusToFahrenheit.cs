using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Edge.Utils.Conversion
{
    public class CelsiusToFahrenheit : IDoubleConverter
    {
        public double Convert(double value)
        {
            return value * (9.0 / 5.0) + 32;
        }
    }
}
