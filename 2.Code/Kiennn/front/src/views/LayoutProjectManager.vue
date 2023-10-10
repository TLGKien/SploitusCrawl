<template>
  <KTDataTable
    @on-sort="sortProject"
    @on-refresh="refreshProject"
    :header= "tableHeader"
    :data= "tableData"
    :itemsPerPage="10"
    :itemsPerPageDropdownEnabled="true"
    ></KTDataTable>
</template>

<script lang="ts">
import { defineComponent,onMounted,ref } from "vue";

import ApiService from "@/core/services/ApiService.ts";
import KTDataTable from "@/components/kt-datatable/KTDataTable.vue";
import arraySort from "array-sort";
import type { Sort } from "@/components/kt-datatable/table-partials/models";


export default defineComponent({
  name: "widgets-tables",
  setup(){
    
      const tableHeader = [
        // Define your table headers here
        { columnName: 'Dự án', columnLabel: 'projectName', sortEnabled: true, columnWidth: 20 },
        { columnName: 'Đối tác', columnLabel: 'partner', sortEnabled: true, columnWidth: 20 },
        { columnName: 'Người phụ trách', columnLabel: 'manager', sortEnabled: true, columnWidth: 200 },
        { columnName: 'Ngày bắt đầu', columnLabel: 'startDate', sortEnabled: true, columnWidth: 20 },
        { columnName: 'Ngày hết hạn', columnLabel: 'dueDate', sortEnabled: true, columnWidth: 20 },
        { columnName: 'Ngân sách', columnLabel: 'budget', sortEnabled: true, columnWidth: 20 },
        { columnName: 'Trạng thái', columnLabel: 'status', sortEnabled: true, columnWidth: 20 },
        { columnName: 'Hành động', columnLabel: 'actions', sortEnabled: false, columnWidth: 20 },
      ];
    const projects = ref([]);

    const sortProject = (sort: Sort) => {
      const reverse: boolean = sort.order === "asc";
      if (sort.label) {
        arraySort(projects.value, sort.label, { reverse });
      }
    };
    // const onItemSelect = (selectedItems: Array<number>) => {
    //   selectedIds.value = selectedItems;
    //   console.log(selectedIds.value);
    // };

    const getAllProject = async () => {
      await ApiService.get("project")
       .then((response) => {
        projects.value = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
    };

    const refreshProject = () => {
      getAllProject()
    };

    onMounted( () => {
      getAllProject();
    });
    
    return {
      tableHeader,
      tableData: projects,
      refreshProject,
      sortProject,
    };
  },
  components: {
    KTDataTable,
  },
});
</script>
