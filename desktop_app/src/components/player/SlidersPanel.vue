<template>
  <div class="slider-container">
    {{ currentTimeConverted }}
    <player-slider
      min="0"
      max="100"
      step="0.4"
      :value="(currentTime / duration) * 100"
      @input="updateCurrentTime"
      class="seek-slider"
    ></player-slider>
    {{ durationTimeConverted }}
  </div>
  <div class="slider-container">
    <volume-down-icon></volume-down-icon>
    <player-slider
      min="0"
      max="100"
      :value="volumeValue"
      @input="updateVolumeValue"
      class="volume-slider"
    />
    <volume-up-icon></volume-up-icon>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import VolumeUpIcon from "@/components/UI/icons/VolumeUpIcon.vue";
import VolumeDownIcon from "@/components/UI/icons/VolumeDownIcon.vue";

export default defineComponent({
  components: {
    VolumeUpIcon,
    VolumeDownIcon,
  },
  props: {
    currentTime: [String, Number],
    volumeValue: [String, Number],
    duration: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      currentTimeInProcents: 0,
    };
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
  width: 400px;
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
</style>
