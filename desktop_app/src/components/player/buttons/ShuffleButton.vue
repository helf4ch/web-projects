<template>
  <player-button @click="switchShuffleOnAndOf">
    <shuffle-icon :class="{ active: isShuffleTurnOn }"></shuffle-icon>
  </player-button>
</template>

<script>
import { defineComponent } from "vue";
import ShuffleIcon from "@/components/UI/icons/ShuffleIcon.vue";
import { mapMutations, mapState } from "vuex";

export default defineComponent({
  components: {
    ShuffleIcon,
  },
  methods: {
    ...mapMutations({
      switchShuffleOnAndOf: "player/switchShuffleOnAndOf",
    }),
  },
  computed: {
    ...mapState({
      isShuffleTurnOn: (state) => state.player.isShuffleTurnOn,
    }),
  },
});
</script>

<style scoped>
.active {
  color: #fabd2f;
}
</style>
