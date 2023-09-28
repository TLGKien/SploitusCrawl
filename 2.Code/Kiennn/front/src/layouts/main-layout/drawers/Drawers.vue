<template>
  <KTMessengerDrawer />
  <KTActivityDrawer />
  <KTToolButtons />
  <KTHelpDrawer />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import KTMessengerDrawer from "@/layouts/main-layout/extras/MessengerDrawer.vue";
import KTActivityDrawer from "@/layouts/main-layout/drawers/ActivityDrawer.vue";
import KTHelpDrawer from "@/layouts/main-layout/extras/HelpDrawer.vue";
import KTToolButtons from "@/layouts/main-layout/extras/ToolButtons.vue";

export default defineComponent({
  name: "global-drawers",
  components: {
    KTMessengerDrawer,
    KTActivityDrawer,
    KTHelpDrawer,
    KTToolButtons,
  },
});
</script>
