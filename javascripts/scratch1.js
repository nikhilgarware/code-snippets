const test = {
  waterFlowMeter: {
    main: "water_flow_meter_list",
    sub: "sub_water_flow_meter_list",
  },
  airMeter: {
    main: "air_flow_meter_list",
    sub: "sub_air_flow_meter_list",
  },
};

console.log(test["waterFlowMeter"]["main"]);

const waterMeterResponse = {
  water_flow_meter_list: [
    {
      name: "water flow meter 1",
      id: 1,
      water_meter_type: 8,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "water flow meter 2",
      id: 2,
      water_meter_type: 9,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "water flow meter 3",
      id: 3,
      water_meter_type: 10,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
  ],
  sub_water_flow_meter_list: [
    {
      name: "sub water flow meter 1",
      id: 1,
      water_meter_type: 1,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "sub water flow meter 2",
      id: 2,
      water_meter_type: 1,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "sub water flow meter 3",
      id: 3,
      water_meter_type: 1,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "sub water flow meter 4",
      id: 4,
      water_meter_type: 1,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "sub water flow meter 5",
      id: 5,
      water_meter_type: 1,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "sub water flow meter 6",
      id: 6,
      water_meter_type: 1,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "sub water flow meter 7",
      id: 7,
      water_meter_type: 1,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "sub water flow meter 8",
      id: 8,
      water_meter_type: 1,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
    {
      name: "sub water flow meter 9",
      id: 9,
      water_meter_type: 1,
      application_details__first_meter_reading_timestamp: 1635079675,
    },
  ],
};
