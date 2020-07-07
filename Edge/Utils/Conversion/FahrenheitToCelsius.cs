using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Edge.Utils.Conversion
{
    public class FahrenheitToCelsius : IDoubleConverter
    {
        public double Convert(double value)
        {
            return (value - 32) * (5.0 / 9.0);
        }
    }
}
