<template>
  <div class="equaliser-panel">
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
    </div>
    <player-switch-button
      :checked="isEqualiserTurnOn"
      @input="switchEqualiserOnAndOf"
    ></player-switch-button>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapMutations, mapState } from "vuex";

export default defineComponent({
  props: {
    equaliserGainValues: {
      type: Array,
      required: true,
    },
  },
  methods: {
    ...mapMutations({
      switchEqualiserOnAndOf: "player/switchEqualiserOnAndOf",
    }),
  },
  computed: {
    ...mapState({
      isEqualiserTurnOn: (state) => state.player.isEqualiserTurnOn,
    }),
  },
});
</script>

<style scoped>
.equaliser-panel {
  min-width: 200px;
  height: 200px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  padding: 5px 0px;
}

.slider-container {
  height: 125px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px 0;
}

.slider {
  margin: 0px -30px !important;
  transform: rotate(-90deg);
  width: 100px;
  position: relative;
  display: inline-block;
}
</style>
