/**
 * This function is to demonstrate the difference between map reduce and filter operator of javascript
 * For more imformation refer https://www.freecodecamp.org/news/javascript-map-reduce-and-filter-explained-with-examples/
 */
function mapReduceFiler() {
  const dataSet = [20, 50, 90, 12, 10, 45, 9, 70.65];
  const mapResult = dataSet.map((items) => {
    return items; // will return all the elements one by one
  });
  const filterResult = dataSet.filter((items) => {
    return items % 2 === 0; // will return elements with applied condition only
  });
  const reduceResult = dataSet.reduce((result, items) => {
    return result + items; // will return sum of all dataset
  });
  console.log(
    "Result of Map",
    mapResult,
    "Result of Filer",
    filterResult,
    "Result of Reduce",
    reduceResult
  );
}
mapReduceFiler();
