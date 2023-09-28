<template>
  <template v-for="(item, i) in MainMenuConfig" :key="i">
    <template v-if="!item.heading">
      <template v-for="(menuItem, j) in item.pages" :key="j">
        <div v-if="menuItem.heading" class="menu-item me-lg-1">
          <router-link
            v-if="menuItem.route"
            class="menu-link"
            :to="menuItem.route"
            active-class="active"
          >
            <span class="menu-title">{{ translate(menuItem.heading) }}</span>
          </router-link>
        </div>
      </template>
    </template>
    
  </template>

</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import { useI18n } from "vue-i18n";
import MainMenuConfig from "@/core/config/MainMenuConfig";
import { headerMenuIcons } from "@/core/helpers/config";

export default defineComponent({
  name: "KTMenu",
  components: {},
  setup() {
    const { t, te } = useI18n();
    const route = useRoute();

    const hasActiveChildren = (match: string) => {
      return route.path.indexOf(match) !== -1;
    };

    const translate = (text: string) => {
      if (te(text)) {
        return t(text);
      } else {
        return text;
      }
    };

    return {
      hasActiveChildren,
      headerMenuIcons,
      MainMenuConfig,
      translate,
      getAssetPath,
    };
  },
});
</script>
