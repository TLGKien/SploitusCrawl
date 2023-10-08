<template>
  <div  class="card">
    <!--begin::Header-->
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Dự án</span>
      </h3>
      <div class="card-toolbar">
        <!--begin::Menu-->
        <a
          href="#"
          class="btn btn-sm fw-bold btn-primary"
          data-bs-toggle="modal"
          data-bs-target="#kt_modal_add_project"
          >Thêm dự án</a
        >
        <!--end::Menu-->
      </div>
    </div>
    <!--end::Header-->

    <!-- start table -->
    <div class="card-body py-3">
      <div class="dataTables_wrapper dt-bootstrap4 no-footer">
        <TableContent
          @on-items-select="onItemSelect"
          @on-sort="onSort"
          :header="header"
          :data="dataToDisplay"
          :checkboxEnabled="checkboxEnabled"
          :checkboxLabel="checkboxLabel"
          :empty-table-text="emptyTableText"
          :sort-label="sortLabel"
          :sort-order="sortOrder"
          :loading="loading"
        >
          <template v-for="(_, name) in $slots" v-slot:[name]="{ row: item }">
            <slot :name="name" :row="item" />
          </template>
        </TableContent>
        <TableFooter
          @page-change="pageChange"
          :current-page="currentPage"
          v-model:itemsPerPage="itemsInTable"
          :count="totalItems"
          :items-per-page-dropdown-enabled="itemsPerPageDropdownEnabled"
        />
      </div>
    </div>
    <!-- end table -->
  </div>
  <AddProjectModal />

</template>

<script lang="ts">
import { computed, defineComponent, ref, watch } from "vue";
import TableContent from "@/components/kt-datatable/table-partials/table-content/TableContent.vue";
import TableFooter from "@/components/kt-datatable/table-partials/TableFooter.vue";
import AddProjectModal from "@/components/modals/forms/AddProjectModal.vue";
import type { Sort } from "@/components/kt-datatable/table-partials/models";

export default defineComponent({
  name: "kt-datatable",
  props: {
    header: { type: Array, required: true },
    data: { type: Array, required: true },
    itemsPerPage: { type: Number, default: 10 },
    itemsPerPageDropdownEnabled: {
      type: Boolean,
      required: false,
      default: true,
    },
    checkboxEnabled: { type: Boolean, required: false, default: false },
    checkboxLabel: { type: String, required: false, default: "id" },
    total: { type: Number, required: false },
    loading: { type: Boolean, required: false, default: false },
    sortLabel: { type: String, required: false, default: null },
    sortOrder: {
      type: String as () => "asc" | "desc",
      required: false,
      default: "asc",
    },
    emptyTableText: { type: String, required: false, default: "No data found" },
    currentPage: { type: Number, required: false, default: 1 },
  },
  emits: [
    "page-change",
    "on-sort",
    "on-items-select",
    "on-items-per-page-change",
  ],
  components: {
    TableContent,
    TableFooter,
    AddProjectModal,
  },
  setup(props, { emit }) {
    const currentPage = ref(props.currentPage);
    const itemsInTable = ref<number>(props.itemsPerPage);

    watch(
      () => itemsInTable.value,
      (val) => {
        currentPage.value = 1;
        emit("on-items-per-page-change", val);
      }
    );

    const pageChange = (page: number) => {
      currentPage.value = page;
      emit("page-change", page);
    };

    const dataToDisplay = computed(() => {
      if (props.data) {
        if (props.data.length <= itemsInTable.value) {
          return props.data;
        } else {
          let sliceFrom = (currentPage.value - 1) * itemsInTable.value;
          return props.data.slice(sliceFrom, sliceFrom + itemsInTable.value);
        }
      }
      return [];
    });

    const totalItems = computed(() => {
      if (props.data) {
        if (props.data.length <= itemsInTable.value) {
          return props.total;
        } else {
          return props.data.length;
        }
      }
      return 0;
    });

    const onSort = (sort: Sort) => {
      emit("on-sort", sort);
    };

    //eslint-disable-next-line
    const onItemSelect = (selectedItems: any) => {
      emit("on-items-select", selectedItems);
    };

    return {
      pageChange,
      dataToDisplay,
      onSort,
      onItemSelect,
      itemsInTable,
      totalItems,
    };
  },
});
</script>
