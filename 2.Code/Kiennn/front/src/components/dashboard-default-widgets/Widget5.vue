<template>
  <div class="card card-flush" :class="className">
    <!--begin::Body-->
    <div
      class="card-body d-flex flex-column justify-content-between mt-9 bgi-no-repeat bgi-size-cover bgi-position-x-center pb-0"
      :style="`background-position: 100% 50%;
        background-image: url('${getAssetPath(
          '/media/stock/900x600/42.png'
        )}');`"
    >
      <!--begin::Wrapper-->
      <div class="mb-20">
        <!--begin::Title-->
        <div class="fs-2hx fw-bold text-gray-800 text-center mb-13">
          <span class="me-2">
            Welcome to
            
            <span class="position-relative d-inline-block text-danger">
              <router-link
                to="/projectManager"
                class="text-danger opacity-75-hover"
                >Project Manager</router-link
              >
              <!--begin::Separator-->
              <span
                class="position-absolute opacity-15 bottom-0 start-0 border-4 border-danger border-bottom w-100"
              ></span>
              <!--end::Separator-->
            </span> </span
          >
        </div>
        <!--end::Title-->


      </div>
      <!--begin::Wrapper-->

      <!--begin::Illustration-->
      <img
        class="mx-auto h-150px h-lg-200px theme-light-show"
        :src="getAssetPath('media/illustrations/misc/upgrade.svg')"
        alt=""
      />
      <img
        class="mx-auto h-200px h-lg-250px theme-dark-show"
        :src="getAssetPath('media/illustrations/misc/upgrade-dark.svg')"
        alt=""
      />
      <!--end::Illustration-->
    </div>
    <!--end::Body-->
  </div>
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";

export default defineComponent({
  name: "default-dashboard-widget-5",
  components: {},
  props: {
    className: { type: String, required: false },
  },
  setup() {
    return {
      getAssetPath,
    };
  },
});
</script>
