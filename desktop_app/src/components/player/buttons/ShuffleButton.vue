<template>
  <player-button>
    <shuffle-icon
      v-if="isShuffleTurnOn"
      class="active"
      @click="switchShuffleOnAndOf"
    ></shuffle-icon>
    <shuffle-icon v-else @click="switchShuffleOnAndOf"></shuffle-icon>
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
