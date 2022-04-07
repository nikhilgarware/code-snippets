const meterList = {
  ht_meter: [
    { name: "ht meter 1", id: 1, meterFirstDate: 1609833628, type: "ht_meter" },
    { name: "ht meter 2", id: 2, meterFirstDate: 1609828996, type: "ht_meter" },
    { name: "ht meter 3", id: 3, meterFirstDate: 1609828996, type: "ht_meter" },
    { name: "ht meter 4", id: 4, meterFirstDate: 1609828996, type: "ht_meter" },
    { name: "ht meter 5", id: 5, meterFirstDate: 1609828996, type: "ht_meter" },
    {
      name: "Sub Meter 1 Default",
      id: 6,
      meterFirstDate: 1609828996,
      connectedHtMeter: 1,
    },
    { name: "Sub Meter 2 DG", id: 7, meterFirstDate: 1609828996 },
    {
      name: "Sub Meter 3 Solar",
      id: 8,
      meterFirstDate: 1609828996,
      connectedHtMeter: 3,
    },
  ],
  sub_meter: [
    { name: "Sub Meter 1 Default", id: 6, meterFirstDate: 1609828996 },
    { name: "Sub Meter 2 DG", id: 7, meterFirstDate: 1609828996 },
    { name: "Sub Meter 3 Solar", id: 8, meterFirstDate: 1609828996 },
    {
      name: "sub meter 4 Air Compressor",
      id: 4,
      meterFirstDate: 1609828996,
    },
    { name: "sub meter 5", id: 5, meterFirstDate: 1609828996 },
    { name: "sub meter 6", id: 6, meterFirstDate: 1609828996 },
    { name: "sub meter 7", id: 7, meterFirstDate: 1609828996 },
    { name: "sub meter 8", id: 8, meterFirstDate: 1609828996 },
    { name: "sub meter 9", id: 9, meterFirstDate: 1609828996 },
    { name: "sub meter 10", id: 10, meterFirstDate: 1609828996 },
    { name: "sub meter 11", id: 11, meterFirstDate: 1609828996 },
    { name: "sub meter 12", id: 12, meterFirstDate: 1609828996 },
    { name: "sub meter 13", id: 13, meterFirstDate: 1609828996 },
    { name: "sub meter 14", id: 14, meterFirstDate: 1609828996 },
    { name: "sub meter 15", id: 15, meterFirstDate: 1609828996 },
    { name: "sub meter 16", id: 16, meterFirstDate: 1609828996 },
    { name: "sub meter 17", id: 17, meterFirstDate: 1609828996 },
    { name: "sub meter 18", id: 18, meterFirstDate: 1609828996 },
    { name: "sub meter 19", id: 19, meterFirstDate: 1609828996 },
    { name: "sub meter 20", id: 20, meterFirstDate: 1609828996 },
    { name: "sub meter 21", id: 21, meterFirstDate: 1609828996 },
    { name: "sub meter 22", id: 22, meterFirstDate: 1609828996 },
    { name: "sub meter 23", id: 23, meterFirstDate: 1609828996 },
    { name: "sub meter 24", id: 24, meterFirstDate: 1609828996 },
    { name: "sub meter 25", id: 25, meterFirstDate: 1609828996 },
    { name: "sub meter 26", id: 26, meterFirstDate: 1609828996 },
    { name: "sub meter 27", id: 27, meterFirstDate: 1609828996 },
    { name: "sub meter 28", id: 28, meterFirstDate: 1609828996 },
    { name: "sub meter 29", id: 29, meterFirstDate: 1609828996 },
    { name: "sub meter 30", id: 30, meterFirstDate: 1609828996 },
    { name: "sub meter 31", id: 31, meterFirstDate: 1609828996 },
    { name: "sub meter 32", id: 32, meterFirstDate: 1609828996 },
    { name: "sub meter 33", id: 33, meterFirstDate: 1609828996 },
    { name: "sub meter 34", id: 34, meterFirstDate: 1609828996 },
    { name: "sub meter 35", id: 35, meterFirstDate: 1609828996 },
  ],
};

function objectFormatter(data) {
  const temp = [];
  const edges = [];
  let initialX = 200;
  let initialY = 100;
  function placeX(presentX) {
    initialX = initialX + 100;
    return presentX + 100;
  }
  function placeY(presentY) {
    initialY = initialY + 100;
    return presentY + 100;
  }
  data.ht_meter.map((items) => {
    temp.push({
      id: String(items.id),
      data: {
        label: items.name,
      },
      position: {
        x: placeX(initialX),
        y: placeY(initialY),
      },
    });
  });
  data.ht_meter.map((iterator) => {
    edges.push({
      id: 1,
      source: String(iterator.id),
      target: String(iterator.connectedHtMeter || iterator.id),
    });
  });
  return edges;
}

console.log(objectFormatter(meterList));
