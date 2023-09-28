<template>
  <!--begin::Row-->

    <!--begin::Col-->
    <div class="col-xxl-12">
      <Widget5 className="h-md-100" />
    </div>
    <!--end::Col-->

  <!--end::Row-->

</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";
import Widget5 from "@/components/dashboard-default-widgets/Widget5.vue";

export default defineComponent({
  name: "main-dashboard",
  components: {
    Widget5,
  },
  setup() {
    return {
      getAssetPath,
    };
  },
});
</script>
