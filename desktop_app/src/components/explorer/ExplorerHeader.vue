<template>
  <div class="explorer-header">
    <player-button
      v-if="prevPath === ''"
      @click="goToPrevPath"
      class="not-active"
      ><arrow-back-icon></arrow-back-icon
    ></player-button>
    <player-button v-else @click="goToPrevPath"
      ><arrow-back-icon></arrow-back-icon
    ></player-button>
    {{ currentPath }}
    <player-button @click="reloadExplorer"
      ><arrow-reload-icon></arrow-reload-icon
    ></player-button>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapState, mapMutations } from "vuex";
import ArrowBackIcon from "@/components/UI/icons/ArrowBackIcon.vue";
import ArrowReloadIcon from "@/components/UI/icons/ArrowReloadIcon.vue";

export default defineComponent({
  components: {
    ArrowBackIcon,
    ArrowReloadIcon,
  },
  emits: ["reloadExplorer"],
  methods: {
    ...mapMutations({
      goToPrevPath: "explorer/goToPrevPath",
    }),
    reloadExplorer() {
      this.$emit("reloadExplorer");
    },
  },
  computed: {
    ...mapState({
      currentPath: (state) => state.explorer.currentPath,
      prevPath: (state) => state.explorer.prevPath,
    }),
  },
});
</script>

<style scoped>
.explorer-header {
  margin: 10px 0;
  padding: 0 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.not-active {
  color: #665c54 !important;
  cursor: default !important;
}

.not-active:hover {
  opacity: 0.8 !important;
}
</style>
