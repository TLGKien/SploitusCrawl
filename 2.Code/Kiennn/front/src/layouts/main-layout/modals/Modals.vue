<template>
  <KTNewTargetModal />
  <KTAddCustomerModal/>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import KTNewTargetModal from "@/components/modals/forms/NewTargetModal.vue";
import KTAddCustomerModal from "@/components/modals/forms/AddCustomerModal.vue";

export default defineComponent({
  name: "global-modals",
  components: {
    KTNewTargetModal,
    KTAddCustomerModal,
  },
});
</script>
