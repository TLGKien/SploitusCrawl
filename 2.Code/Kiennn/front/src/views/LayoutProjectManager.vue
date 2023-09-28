<template>
  <TablesWidget widget-classes="mb-5 mb-xl-8" :tableHeader="tableHeader" :tableData="tableData"></TablesWidget>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import TablesWidget from "@/components/widgets/tables/Widget14.vue";

export default defineComponent({
  name: "widgets-tables",
  data(){
    return {
      tableHeader:[
        // Define your table headers here
        { text: 'Dự án', value: 'title' },
        { text: 'Đối tác', value: 'partner' },
        { text: 'Người phụ trách', value: 'manager' },
        { text: 'Ngày bắt đầu', value: 'startDate' },
        { text: 'Ngày hết hạn', value: 'dueDate' },
        { text: 'Ngân sách', value: 'budget' },
        { text: 'Trạng thái', value: 'status' },
        { text: 'Hành động', value: 'actions' },
      ],
      tableData:[
        {
          project: {
            name: 'Dự án A',
            description:'ajsdgjahfvhjsdbjvasklcjkas asd á da',
          },
          partner: 'Nguyễn văn B',
          manager:'Nguyễn Văn Kiên',
          startDate:'05/28/2020',
          dueDate:'05/28/2020',
          budget:'1500',
          status: {
            label: 'In progess',
            color: 'success',
          },
        },
        {
          project: {
            name: 'Dự án B',
            description:'Đây là mô tả cho dự án B',
          },
          partner: 'Nguyễn văn Hoang Anh',
          manager:'Nguyễn Văn Hoàng',
          startDate:'05/28/2021',
          dueDate:'05/28/2022',
          budget:'5000',
          status: {
            label: 'Pending',
            color: 'pending',
          },
        },
        {
          project: {
            name: 'Dự án C',
            description:'Đây là mô tả cho dự án C',
          },
          partner: 'Nguyễn văn thùy',
          manager:'Nguyễn Văn thanh',
          startDate:'05/28/2022',
          dueDate:'05/28/2023',
          budget:'5100',
          status: {
            label: 'Approved',
            color: 'Approved',
          },
        },
        {
          project: {
            name: 'Dự án A',
            description:'ajsdgjahfvhjsdbjvasklcjkas asd á da',
          },
          partner: 'Nguyễn văn B',
          manager:'Nguyễn Văn Kiên',
          startDate:'05/28/2020',
          dueDate:'05/28/2020',
          budget:'1500',
          status: {
            label: 'In progess',
            color: 'success',
          },
        },
        {
          project: {
            name: 'Dự án B',
            description:'Đây là mô tả cho dự án B',
          },
          partner: 'Nguyễn văn Hoang Anh',
          manager:'Nguyễn Văn Hoàng',
          startDate:'05/28/2021',
          dueDate:'05/28/2022',
          budget:'5000',
          status: {
            label: 'Pending',
            color: 'pending',
          },
        },
        {
          project: {
            name: 'Dự án C',
            description:'Đây là mô tả cho dự án C',
          },
          partner: 'Nguyễn văn thùy',
          manager:'Nguyễn Văn thanh',
          startDate:'05/28/2022',
          dueDate:'05/28/2023',
          budget:'5100',
          status: {
            label: 'Approved',
            color: 'Approved',
          },
        },
      ],
    };
  },
  components: {
    TablesWidget,
  },
});
</script>
