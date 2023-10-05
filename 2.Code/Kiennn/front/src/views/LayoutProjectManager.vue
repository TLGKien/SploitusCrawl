<template>
  <TablesWidget widget-classes="mb-5 mb-xl-8" :tableHeader="tableHeader" :tableData="tableData"></TablesWidget>
</template>

<script lang="ts">
import { defineComponent,onMounted,ref } from "vue";

import TablesWidget from "@/components/widgets/tables/Widget14.vue";
import ApiService from "@/core/services/ApiService.ts";

export default defineComponent({
  name: "widgets-tables",
  setup(){
    const projects = ref([]);
    const tableHeader = [
        // Define your table headers here
        { text: 'Dự án', value: 'title' },
        { text: 'Đối tác', value: 'partner' },
        { text: 'Người phụ trách', value: 'manager' },
        { text: 'Ngày bắt đầu', value: 'startDate' },
        { text: 'Ngày hết hạn', value: 'dueDate' },
        { text: 'Ngân sách', value: 'budget' },
        { text: 'Trạng thái', value: 'status' },
        { text: 'Hành động', value: 'actions' },
      ];

    onMounted(async () => {
      await ApiService.get("project")
       .then((response) => {
        projects.value = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
    });
    
    return {
      tableHeader:tableHeader,
      tableData: projects,
    };
  },
  components: {
    TablesWidget,
  },
});
</script>
