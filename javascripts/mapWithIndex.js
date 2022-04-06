// const data = [12, 12, 12, 12, 12];

// data.map((index, data) => {
//   console.log(data);
// });

const test = {
  flow_meter_summary_for_huber: {
    reportName: "Main Reports",
    reports: {
      flow_meter_summary_for_huber: "UIS Flow Meter Summary",
      huber_ems_summary: "EMS Summary Report",
    },
  },
};

Object.keys(test).map((data) => {
  //   console.log(data);
  //   console.log(test[data].reportName);
  //   console.log(
  //     Object.keys(test[data].reports).map((item) => {
  //       return item;
  //     })
  //   );
  console.log(...data);
});
