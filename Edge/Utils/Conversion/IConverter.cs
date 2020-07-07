using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Edge.Utils.Conversion
{
    /// <summary>
    /// Interface for multiple conversion
    /// </summary>
    /// <typeparam name="FROM">The origin type of the data</typeparam>
    /// <typeparam name="TO">The output type of the data</typeparam>
    internal interface IConverter<FROM, TO>
    {
        /// <summary>
        /// Convert a value to another
        /// </summary>
        /// <param name="value">The value to be converted</param>
        /// <returns>The value converted</returns>
        TO Convert(FROM value);
    }

    internal interface IDoubleConverter : IConverter<double, double> { }
}
