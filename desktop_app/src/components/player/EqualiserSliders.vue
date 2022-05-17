<template>
  <div class="slider-container">
    <player-slider
      min="-16"
      max="16"
      step="0.1"
      class="slider"
      v-for="gainValue in equaliserGainValues"
      :key="gainValue.id"
      :value="gainValue.gain"
      @input="$emit('changeGainValueById', gainValue.id, $event.target.value)"
    />
    <!-- @input="$emit('changeGainValueById', gainValue.id, event.target.value)" -->
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
  margin: 0px -30px !important;
  transform: rotate(-90deg);
  width: 100px;
  position: relative;
  display: inline-block;
}
</style>
