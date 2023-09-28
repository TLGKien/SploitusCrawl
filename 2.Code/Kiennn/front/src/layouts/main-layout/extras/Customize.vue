<template>
  <button
    id="kt_app_layout_builder_toggle"
    class="btn btn-dark app-layout-builder-toggle lh-1 py-4"
    data-bs-toggle="tooltip"
    data-bs-placement="left"
    data-bs-dismiss="click"
    data-bs-trigger="hover"
  >
    <KTIcon icon-name="setting-4" icon-class="fs-4 me-1" />Customize
  </button>

  <div
    id="kt_app_layout_builder"
    class="bg-body drawer drawer-end"
    data-kt-drawer="true"
    data-kt-drawer-name="app-settings"
    data-kt-drawer-activate="true"
    data-kt-drawer-overlay="true"
    data-kt-drawer-width="{default:'300px', 'lg': '380px'}"
    data-kt-drawer-direction="end"
    data-kt-drawer-toggle="#kt_app_layout_builder_toggle"
    data-kt-drawer-close="#kt_app_layout_builder_close"
  >
    <!--begin::Card-->
    <div class="card border-0 shadow-none rounded-0 w-100">
      <!--begin::Card header-->
      <div
        class="card-header bgi-position-y-bottom bgi-position-x-end bgi-size-cover bgi-no-repeat rounded-0 border-0 py-4"
        id="kt_app_layout_builder_header"
        :style="{
          backgroundImage: `url(
            ${getAssetPath('media/misc/layout/customizer-header-bg.jpg')}
          )`,
        }"
      >
        <!--begin::Card title-->
        <h3 class="card-title fs-3 fw-bold text-white flex-column m-0">
          Metronic Builder
          <small class="text-white opacity-50 fs-7 fw-semibold pt-1"
            >Get your product deeply customized</small
          >
        </h3>
        <!--end::Card title-->
        <!--begin::Card toolbar-->
        <div class="card-toolbar">
          <button
            type="button"
            class="btn btn-sm btn-icon bg-white bg-opacity-25 btn-color-white p-0 w-20px h-20px rounded-1"
            id="kt_app_layout_builder_close"
          >
            <KTIcon icon-name="cross-square" icon-class="fs-3" />
          </button>
        </div>
        <!--end::Card toolbar-->
      </div>
      <!--end::Card header-->
      <!--begin::Card body-->
      <div class="card-body position-relative" id="kt_app_layout_builder_body">
        <!--begin::Content-->
        <div
          id="kt_app_settings_content"
          class="position-relative scroll-y me-n5 pe-5"
          data-kt-scroll="true"
          data-kt-scroll-height="auto"
          data-kt-scroll-wrappers="#kt_app_layout_builder_body"
          data-kt-scroll-dependencies="#kt_app_layout_builder_header, #kt_app_layout_builder_footer"
          data-kt-scroll-offset="5px"
          style="height: 710px"
        >
          <!--begin::Form-->
          <form class="form" id="kt_app_layout_builder_form">
            <input
              type="hidden"
              id="kt_app_layout_builder_action"
              name="layout-builder[action]"
            />
            <!--begin::Card body-->
            <div class="card-body p-0">
              <!--begin::Form group-->
              <div class="form-group">
                <!--begin::Heading-->
                <div class="mb-6">
                  <h4 class="fw-bold text-dark">Theme Mode</h4>
                  <div class="fw-semibold text-muted fs-7 d-block lh-1">
                    Enjoy Dark &amp; Light modes.
                  </div>
                </div>
                <!--end::Heading-->
                <!--begin::Options-->
                <div
                  class="row"
                  data-kt-buttons="true"
                  data-kt-buttons-target=".form-check-image,.form-check-input"
                  data-kt-initialized="1"
                >
                  <!--begin::Col-->
                  <div class="col-6">
                    <!--begin::Option-->
                    <label
                      :class="[themeMode === 'light' && 'active']"
                      class="form-check-image form-check-success"
                    >
                      <!--begin::Image-->
                      <div class="form-check-wrapper">
                        <img
                          :src="
                            getAssetPath('media/misc/layout/demo1-light.png')
                          "
                          class="mw-100"
                          alt=""
                        />
                      </div>
                      <!--end::Image-->
                      <!--begin::Check-->
                      <div
                        class="form-check form-check-custom form-check-solid form-check-sm form-check-success"
                      >
                        <input
                          :checked="themeMode === 'light' ? undefined : false"
                          @change="onThemeModeChange"
                          class="form-check-input"
                          type="radio"
                          value="light"
                          name="theme_mode"
                        />
                        <!--begin::Label-->
                        <div class="form-check-label text-gray-700">Light</div>
                        <!--end::Label-->
                      </div>
                      <!--end::Check-->
                    </label>
                    <!--end::Option-->
                  </div>
                  <!--end::Col-->
                  <!--begin::Col-->
                  <div class="col-6">
                    <!--begin::Option-->
                    <label
                      :class="[themeMode === 'dark' && 'active']"
                      class="form-check-image form-check-success"
                    >
                      <!--begin::Image-->
                      <div class="form-check-wrapper">
                        <img
                          :src="
                            getAssetPath('media/misc/layout/demo1-dark.png')
                          "
                          class="mw-100"
                          alt=""
                        />
                      </div>
                      <!--end::Image-->
                      <!--begin::Check-->
                      <div
                        class="form-check form-check-custom form-check-solid form-check-sm form-check-success"
                      >
                        <input
                          @change="onThemeModeChange"
                          :checked="themeMode === 'dark' ? undefined : false"
                          class="form-check-input"
                          type="radio"
                          value="dark"
                          name="theme_mode"
                        />
                        <!--begin::Label-->
                        <div class="form-check-label text-gray-700">Dark</div>
                        <!--end::Label-->
                      </div>
                      <!--end::Check-->
                    </label>
                    <!--end::Option-->
                  </div>
                  <!--end::Col-->
                </div>
                <!--end::Options-->
              </div>
              <!--end::Form group-->
              <!--begin::Separator-->
              <div class="separator separator-dashed my-5"></div>
              <!--end::Separator-->
              <!--begin::Form group-->
              <div class="form-group">
                <!--begin::Heading-->
                <div class="d-flex flex-column mb-4">
                  <h4 class="fw-bold text-dark">Width Mode</h4>
                  <div class="fs-7 fw-semibold text-muted">
                    Page width options
                  </div>
                </div>
                <!--end::Heading-->
                <!--begin::Options-->
                <div class="d-flex">
                  <!--begin::Check-->
                  <div
                    class="form-check form-check-custom form-check-success form-check-solid form-check-sm me-5"
                  >
                    <input
                      v-model="config.general.pageWidth"
                      class="form-check-input"
                      type="radio"
                      value="default"
                      id="kt_builder_page_width_default"
                    />
                    <!--begin::Label-->
                    <label
                      class="form-check-label text-gray-700 fw-bold text-nowrap"
                      for="kt_builder_page_width_default"
                      >Default</label
                    >
                    <!--end::Label-->
                  </div>
                  <!--end::Check-->
                  <!--begin::Check-->
                  <div
                    class="form-check form-check-custom form-check-success form-check-solid form-check-sm me-5"
                  >
                    <input
                      v-model="config.general.pageWidth"
                      class="form-check-input"
                      type="radio"
                      value="fluid"
                      id="kt_builder_page_width_fluid"
                    />
                    <!--begin::Label-->
                    <label
                      class="form-check-label text-gray-700 fw-bold text-nowrap"
                      for="kt_builder_page_width_fluid"
                      >Fluid</label
                    >
                    <!--end::Label-->
                  </div>
                  <!--end::Check-->
                  <!--begin::Check-->
                  <div
                    class="form-check form-check-custom form-check-success form-check-solid form-check-sm me-5"
                  >
                    <input
                      v-model="config.general.pageWidth"
                      class="form-check-input"
                      type="radio"
                      value="fixed"
                      id="kt_builder_page_width_fixed"
                    />
                    <!--begin::Label-->
                    <label
                      class="form-check-label text-gray-700 fw-bold text-nowrap"
                      for="kt_builder_page_width_fixed"
                      >Fixed</label
                    >
                    <!--end::Label-->
                  </div>
                  <!--end::Check-->
                </div>
                <!--end::Options-->
              </div>
              <!--end::Form group-->
              <!--begin::Separator-->
              <div class="separator separator-dashed my-5"></div>
              <!--end::Separator-->
              <!--begin::Form group-->
              <div class="form-group">
                <!--begin::Heading-->
                <div class="d-flex flex-column mb-4">
                  <h4 class="fw-bold text-dark">Keenicons Style</h4>
                  <div>
                    <span class="fs-7 fw-semibold text-muted"
                      >Select global UI icons style.</span
                    >
                    <a
                      class="fw-semibold"
                      href="https://preview.keenthemes.com/html/metronic/docs/icons/keenicons"
                      target="_blank"
                      >Learn more</a
                    >
                  </div>
                </div>
                <!--end::Heading-->
                <!--begin::Options-->
                <div class="d-flex flex-stack gap-3">
                  <!--begin::Option-->
                  <label
                    :class="config.general.iconsType === 'duotone' && 'active'"
                    class="form-check-image form-check-success w-100 parent-active parent-hover"
                  >
                    <!--begin::Image-->
                    <div
                      class="form-check-wrapper d-flex flex-center border-gray-200 border-2 mb-0 py-3 px-4"
                    >
                      <KTIcon
                        icon-type="duotone"
                        icon-name="picture"
                        icon-class="fs-1 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                      />
                      <span
                        class="fs-7 fw-semibold ms-2 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                        >Duotone</span
                      >
                    </div>
                    <!--end::Image-->
                    <!--begin::Check-->
                    <div
                      style="
                        visibility: hidden;
                        height: 0;
                        width: 0;
                        overflow: hidden;
                      "
                    >
                      <input
                        v-model="config.general.iconsType"
                        class="form-check-input"
                        type="radio"
                        value="duotone"
                        :checked="config.general.iconsType === 'duotone'"
                        name="duotone"
                      />
                    </div>
                    <!--end::Check-->
                  </label>
                  <!--end::Option-->
                  <!--begin::Option-->
                  <label
                    :class="config.general.iconsType === 'outline' && 'active'"
                    class="form-check-image form-check-success w-100 parent-active parent-hover"
                  >
                    <!--begin::Image-->
                    <div
                      class="form-check-wrapper d-flex flex-center border-gray-200 border-2 mb-0 py-3 px-4"
                    >
                      <KTIcon
                        icon-type="outline"
                        icon-name="picture"
                        icon-class="fs-1 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                      />
                      <span
                        class="fs-7 fw-semibold ms-2 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                        >Outline</span
                      >
                    </div>
                    <!--end::Image-->
                    <!--begin::Check-->
                    <div
                      style="
                        visibility: hidden;
                        height: 0;
                        width: 0;
                        overflow: hidden;
                      "
                    >
                      <input
                        v-model="config.general.iconsType"
                        class="form-check-input"
                        type="radio"
                        value="outline"
                        name="outline"
                        :checked="config.general.iconsType === 'outline'"
                      />
                    </div>
                    <!--end::Check-->
                  </label>
                  <!--end::Option-->
                  <!--begin::Option-->
                  <label
                    :class="config.general.iconsType === 'solid' && 'active'"
                    class="form-check-image form-check-success w-100 parent-active parent-hover"
                  >
                    <!--begin::Image-->
                    <div
                      class="form-check-wrapper d-flex flex-center border-gray-200 border-2 mb-0 py-3 px-4"
                    >
                      <KTIcon
                        icon-type="solid"
                        icon-name="picture"
                        icon-class="fs-1 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                      />
                      <span
                        class="fs-7 fw-semibold ms-2 text-gray-500 parent-active-gray-700 parent-hover-gray-700"
                        >Solid</span
                      >
                    </div>
                    <!--end::Image-->
                    <!--begin::Check-->
                    <div
                      style="
                        visibility: hidden;
                        height: 0;
                        width: 0;
                        overflow: hidden;
                      "
                    >
                      <input
                        v-model="config.general.iconsType"
                        class="form-check-input"
                        type="radio"
                        value="solid"
                        name="solid"
                        :checked="config.general.iconsType === 'solid'"
                      />
                    </div>
                    <!--end::Check-->
                  </label>
                  <!--end::Option-->
                </div>
                <!--end::Options-->
              </div>
              <!--end::Form group-->
              <!--begin::Separator-->
              <div class="separator separator-dashed my-5"></div>
              <!--end::Separator-->
              <!--begin::Form group-->
              <div class="form-group">
                <!--begin::Heading-->
                <div class="d-flex flex-column mb-4">
                  <h4 class="fw-bold text-dark">Menu Icon</h4>
                  <div class="fs-7 fw-semibold text-muted">
                    Sidebar menu icon options
                  </div>
                </div>
                <!--end::Heading-->
                <!--begin::Options-->
                <div class="d-flex">
                  <!--begin::Check-->
                  <div
                    class="form-check form-check-custom form-check-success form-check-solid form-check-sm me-5"
                  >
                    <input
                      v-model="config.sidebar.default.menu.iconType"
                      class="form-check-input"
                      type="radio"
                      value="keenthemes"
                      id="kt_builder_keenthemes_icons"
                    />
                    <!--begin::Label-->
                    <label
                      class="form-check-label text-gray-700 fw-bold text-nowrap"
                      for="kt_builder_keenthemes_icons"
                      >Keenthemes Icons</label
                    >
                    <!--end::Label-->
                  </div>
                  <!--end::Check-->
                  <!--begin::Check-->
                  <div
                    class="form-check form-check-custom form-check-success form-check-solid form-check-sm me-5"
                  >
                    <input
                      v-model="config.sidebar.default.menu.iconType"
                      class="form-check-input"
                      type="radio"
                      value="bootstrap"
                      id="kt_builder_bootstrap_icons"
                    />
                    <!--begin::Label-->
                    <label
                      class="form-check-label text-gray-700 fw-bold text-nowrap"
                      for="kt_builder_bootstrap_icons"
                      >Bootstrap Icons</label
                    >
                    <!--end::Label-->
                  </div>
                  <!--end::Check-->
                </div>
                <!--end::Options-->
              </div>
              <!--end::Form group-->
              <!--begin::Separator-->
              <div class="separator separator-dashed my-5"></div>
              <!--end::Separator-->
              <!--begin::Form group-->
              <div class="form-group">
                <!--begin::Heading-->
                <div class="mb-6">
                  <h4 class="fw-bold text-dark">Layouts</h4>
                  <span class="fw-semibold text-muted fs-7 lh-1"
                    >4 main layouts.{{ " " }}</span
                  >
                  <router-link to="/builder" class="text-primary"
                    >More layout options</router-link
                  >
                </div>
                <!--end::Heading-->
                <!--begin::Options-->
                <div
                  class="row gy-3"
                  data-kt-buttons="true"
                  data-kt-buttons-target=".form-check-image:not(.disabled),.form-check-input:not([disabled])"
                  data-kt-initialized="1"
                >
                  <!--begin::Col-->
                  <div class="col-6">
                    <!--begin::Option-->
                    <label
                      class="form-check-image form-check-success"
                      :class="[layoutType === 'dark-sidebar' && 'active']"
                    >
                      <!--begin::Image-->
                      <div class="form-check-wrapper">
                        <img
                          :src="
                            getAssetPath('media/misc/layout/dark-sidebar.png')
                          "
                          class="mw-100"
                          alt=""
                        />
                      </div>
                      <!--end::Image-->
                      <!--begin::Check-->
                      <div
                        class="form-check form-check-custom form-check-success form-check-sm form-check-solid"
                      >
                        <input
                          v-model="layoutType"
                          class="form-check-input"
                          type="radio"
                          value="dark-sidebar"
                          name="layoutType"
                        />
                        <!--begin::Label-->
                        <div class="form-check-label text-gray-700">
                          Dark Sidebar
                        </div>
                        <!--end::Label-->
                      </div>
                      <!--end::Check-->
                    </label>
                    <!--end::Option-->
                  </div>
                  <!--end::Col-->
                  <!--begin::Col-->
                  <div class="col-6">
                    <!--begin::Option-->
                    <label
                      class="form-check-image form-check-success"
                      :class="[layoutType === 'light-sidebar' && 'active']"
                    >
                      <!--begin::Image-->
                      <div class="form-check-wrapper">
                        <img
                          :src="
                            getAssetPath('media/misc/layout/light-sidebar.png')
                          "
                          class="mw-100"
                          alt=""
                        />
                      </div>
                      <!--end::Image-->
                      <!--begin::Check-->
                      <div
                        class="form-check form-check-custom form-check-success form-check-sm form-check-solid"
                      >
                        <input
                          v-model="layoutType"
                          class="form-check-input"
                          type="radio"
                          value="light-sidebar"
                          name="layoutType"
                        />
                        <!--begin::Label-->
                        <div class="form-check-label text-gray-700">
                          Light Sidebar
                        </div>
                        <!--end::Label-->
                      </div>
                      <!--end::Check-->
                    </label>
                    <!--end::Option-->
                  </div>
                  <!--end::Col-->
                  <!--begin::Col-->
                  <div class="col-6">
                    <!--begin::Option-->
                    <label
                      class="form-check-image form-check-success"
                      :class="[layoutType === 'dark-header' && 'active']"
                    >
                      <!--begin::Image-->
                      <div class="form-check-wrapper">
                        <img
                          :src="
                            getAssetPath('media/misc/layout/dark-header.png')
                          "
                          class="mw-100"
                          alt=""
                        />
                      </div>
                      <!--end::Image-->
                      <!--begin::Check-->
                      <div
                        class="form-check form-check-custom form-check-success form-check-sm form-check-solid"
                      >
                        <input
                          v-model="layoutType"
                          class="form-check-input"
                          type="radio"
                          value="dark-header"
                          name="layoutType"
                        />
                        <!--begin::Label-->
                        <div class="form-check-label text-gray-700">
                          Dark Header
                        </div>
                        <!--end::Label-->
                      </div>
                      <!--end::Check-->
                    </label>
                    <!--end::Option-->
                  </div>
                  <!--end::Col-->
                  <!--begin::Col-->
                  <div class="col-6">
                    <!--begin::Option-->
                    <label
                      class="form-check-image form-check-success"
                      :class="[layoutType === 'light-header' && 'active']"
                    >
                      <!--begin::Image-->
                      <div class="form-check-wrapper">
                        <img
                          :src="
                            getAssetPath('media/misc/layout/light-header.png')
                          "
                          class="mw-100"
                          alt=""
                        />
                      </div>
                      <!--end::Image-->
                      <!--begin::Check-->
                      <div
                        class="form-check form-check-custom form-check-success form-check-sm form-check-solid"
                      >
                        <input
                          v-model="layoutType"
                          class="form-check-input"
                          type="radio"
                          value="light-header"
                          name="layoutType"
                        />
                        <!--begin::Label-->
                        <div class="form-check-label text-gray-700">
                          Light Header
                        </div>
                        <!--end::Label-->
                      </div>
                      <!--end::Check-->
                    </label>
                    <!--end::Option-->
                  </div>
                  <!--end::Col-->
                </div>
                <!--end::Options-->
              </div>
              <!--end::Form group-->
            </div>
            <!--end::Card body-->
          </form>
          <!--end::Form-->
        </div>
        <!--end::Content-->
      </div>
      <!--end::Card body-->
      <!--begin::Card footer-->
      <div
        class="card-footer border-0 d-flex gap-3 pb-9 pt-0"
        id="kt_app_layout_builder_footer"
      >
        <button
          type="button"
          @click="submit"
          id="kt_app_layout_builder_preview"
          class="btn btn-primary flex-grow-1 fw-semibold"
        >
          <!--begin::Indicator label-->
          <span class="indicator-label">Preview</span>
          <!--end::Indicator label-->
        </button>
        <button
          @click="reset"
          type="button"
          id="kt_app_layout_builder_reset"
          class="btn btn-light flex-grow-1 fw-semibold"
        >
          <!--begin::Indicator label-->
          <span class="indicator-label">Reset</span>
          <!--end::Indicator label-->
          <!--begin::Indicator progress-->
          <span class="indicator-progress"
            >Please wait...
            <span
              class="spinner-border spinner-border-sm align-middle ms-2"
            ></span
          ></span>
          <!--end::Indicator progress-->
        </button>
      </div>
      <!--end::Card footer-->
    </div>
    <!--end::Card-->
  </div>
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, ref } from "vue";
import { config, layout, themeMode } from "@/core/helpers/config";
import { LS_CONFIG_NAME_KEY, useConfigStore } from "@/stores/config";
import { useThemeStore } from "@/stores/theme";

export default defineComponent({
  name: "customize-layout",
  components: {},
  setup() {
    const storeConfig = useConfigStore();
    const storeTheme = useThemeStore();

    const layoutType = ref(layout.value);

    /**
     * Reset config
     * @param e
     */
    const reset = (e: Event) => {
      e.preventDefault();
      // remove existing saved config
      localStorage.removeItem(LS_CONFIG_NAME_KEY);
      window.location.reload();
    };

    const onThemeModeChange = (e: Event) => {
      const target = e.target as HTMLInputElement;

      storeConfig.setLayoutConfigProperty("general.mode", target.value);
      storeTheme.setThemeMode(target.value as "dark" | "light" | "system");

      // save new config to localStorage
      localStorage.setItem(LS_CONFIG_NAME_KEY, JSON.stringify(config.value));
    };

    /**
     * Submit form
     * @param event
     */
    const submit = (event: Event) => {
      event.preventDefault();

      storeConfig.setLayoutConfigProperty("general.layout", layoutType);
      // save new config to localStorage
      localStorage.setItem(LS_CONFIG_NAME_KEY, JSON.stringify(config.value));
      window.location.reload();
    };

    return {
      reset,
      onThemeModeChange,
      submit,
      config,
      layoutType,
      themeMode,
      getAssetPath,
    };
  },
});
</script>
