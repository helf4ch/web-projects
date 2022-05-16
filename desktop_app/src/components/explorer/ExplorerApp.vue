<template>
  <div class="explorer">
    <div class="explorer-header">
      {{ currentPath }}
    </div>
    <explorer-element-list
      @changeTrackList="changeTrackList"
    ></explorer-element-list>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapState } from "vuex";

import ExplorerElementList from "@/components/explorer/ExplorerElementList.vue";

export default defineComponent({
  components: {
    ExplorerElementList,
  },
  emits: ["changeTrackList"],
  computed: {
    ...mapState({
      currentPath: (state) => state.explorer.currentPath,
    }),
  },
  methods: {
    changeTrackList() {
      this.$emit("changeTrackList");
    },
  },
});
</script>

<style scoped>
.explorer {
  border-top: 2px solid #665c54;
  margin: 30px 20px;
  padding: 0 25px;
  font-size: 1.1rem;
}

.explorer-header {
  margin: 10px 0;
  text-align: center;
}
</style>
