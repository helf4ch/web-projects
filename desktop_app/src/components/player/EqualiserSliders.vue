<template>
  <div class="slider-container">
    <input
      type="range"
      min="-16"
      max="16"
      step="0.1"
      class="slider"
      :value="gainValue.gain"
      v-for="gainValue in equaliserGainValues"
      :key="gainValue.id"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    equaliserGainValues: {
      type: Array,
      required: true,
    },
  },
});
</script>

<style scoped>
.slider-container {
  min-width: 200px;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px 0px;
}

.slider {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  height: 8px;
  background: #665c54;
  opacity: 0.7;
  -webkit-transition: 0.2s;
  transition: opacity 0.2s;
  border-radius: 5px;
  margin: 0px -30px;
  transform: rotate(-90deg);
  width: 100px;
  position: relative;
  display: inline-block;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: 15px;
  height: 15px;
  background: #ebdbb2;
  cursor: pointer;
  border-radius: 50%;
}

.slider:hover {
  opacity: 1;
}
</style>
