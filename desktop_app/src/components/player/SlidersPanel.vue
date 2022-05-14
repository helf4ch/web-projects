<template>
  <div class="slider-container">
    {{ currentTimeConverted }}
    <input
      type="range"
      min="0"
      max="100"
      class="seek-slider"
      :value="(currentTime / duration) * 100"
      @input="updateCurrentTime"
    />
    {{ durationTimeConverted }}
  </div>
  <div class="slider-container">
    <volume-down-icon></volume-down-icon>
    <input
      type="range"
      min="0"
      max="100"
      class="volume-slider"
      :value="volumeValue"
      @input="updateVolumeValue"
    />
    <volume-up-icon></volume-up-icon>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import VolumeUpIcon from "@/components/UI/icons/VolumeUpIcon.vue";
import VolumeDownIcon from "@/components/UI/icons/VolumeDownIcon.vue";

export default defineComponent({
  components: {
    VolumeUpIcon,
    VolumeDownIcon,
  },
  props: {
    currentTime: [Number],
    volumeValue: [String, Number],
    duration: {
      type: Number,
      required: true,
    },
  },
  emits: ["updateVolumeValue", "updateCurrentTime"],
  methods: {
    updateCurrentTime(event) {
      this.$emit("updateCurrentTime", event.target.value);
    },
    updateVolumeValue(event) {
      this.$emit("updateVolumeValue", event.target.value);
    },
    convertTime(time) {
      if (isNaN(time)) {
        return "00:00";
      }

      let minutes = Math.floor(time / 60);
      let seconds = Math.floor(time - minutes * 60);

      let resultMinutes = minutes.toString();
      let resultSeconds = seconds.toString();

      if (minutes < 10) {
        resultMinutes = "0" + minutes;
      }
      if (seconds < 10) {
        resultSeconds = "0" + seconds;
      }

      return resultMinutes + ":" + resultSeconds;
    },
  },
  computed: {
    durationTimeConverted() {
      return this.convertTime(this.duration);
    },
    currentTimeConverted() {
      return this.convertTime(this.currentTime);
    },
  },
});
</script>

<style scoped>
.slider-container {
  width: 75%;
  max-width: 400px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px 0px;
}

.seek-slider {
  width: 60%;
}

.volume-slider {
  width: 30%;
}

.seek-slider,
.volume-slider {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  height: 8px;
  background: #665c54;
  opacity: 0.7;
  -webkit-transition: 0.2s;
  transition: opacity 0.2s;
  border-radius: 5px;
  margin: 0px 10px;
}

.seek-slider::-webkit-slider-thumb,
.volume-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: 15px;
  height: 15px;
  background: #ebdbb2;
  cursor: pointer;
  border-radius: 50%;
}

.seek-slider:hover,
.volume-slider:hover {
  opacity: 1;
}
</style>
