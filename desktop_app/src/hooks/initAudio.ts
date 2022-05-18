export function initAudio() {
  const audioElement = document.createElement("audio");
  const audioContext = new AudioContext();
  const audioSource = audioContext.createMediaElementSource(audioElement);
  const analyser = audioContext.createAnalyser();

  function createFilter(frequency) {
    const filter = audioContext.createBiquadFilter();

    filter.type = "peaking";
    filter.frequency.value = frequency;
    filter.Q.value = 1;
    filter.gain.value = 0;

    return filter;
  }

  function createFilters() {
    const frequencies = [
      60, 170, 310, 600, 1000, 3000, 6000, 12000, 14000, 16000,
    ];
    const filters = frequencies.map(createFilter);

    filters.reduce(function (prev, curr) {
      prev.connect(curr);
      return curr;
    });

    return filters;
  }

  const filters = createFilters();

  audioSource.connect(filters[0]);
  audioSource.connect(analyser);
  filters[filters.length - 1].connect(audioContext.destination);
  analyser.connect(audioContext.destination);

  analyser.fftSize = 32;
  const visualiserDataArray = new Uint8Array(analyser.frequencyBinCount);

  return {
    audioElement,
    // audioContext,
    // audioSource,
    analyser,
    filters,
    visualiserDataArray,
  };
}
