import { createApp } from "vue";
import App from "@/App.vue";
import components from "@/components/UI/index";
import store from "@/store/index";

const app = createApp(App);

components.forEach((component) => {
  app.component(component.name, component);
});

app.use(store).mount("#app");
