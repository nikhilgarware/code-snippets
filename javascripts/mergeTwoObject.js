const utility = {
  gasFlowMeter: "gas-meters",
  waterMeter: "water-meters",
  airMeter: "air-meters",
  steamMeter: "steam-meters",
  nitrogenMeter: "nitrogen-meters",
  iceWaterMeter: "ice-water-meters",
  naturalGasMeter: "natural-gas-meters",
  data: {
    data: "data",
  },
};

const electrical = {
  electricalMeter: "electrical-meters",
};

const neutral = { ...utility, ...electrical };
console.log(neutral);
