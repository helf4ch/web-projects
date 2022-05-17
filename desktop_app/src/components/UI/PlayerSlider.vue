<template>
  <input type="range" class="slider" />
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "player-slider",
});
</script>

<style scoped>
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
  margin: 0px 10px;
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
