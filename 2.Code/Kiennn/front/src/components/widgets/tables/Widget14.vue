<template>
  <!--begin::Tables -->
  <div :class="widgetClasses" class="card">
    <!--begin::Header-->
    <div class="card-header border-0 pt-5">
      <h3 class="card-title align-items-start flex-column">
        <span class="card-label fw-bold fs-3 mb-1">Projects</span>
          <span class="text-muted mt-1 fw-semobold fs-7">Over {{ tableData.length }} Projects</span>


      </h3>
      <div class="card-toolbar">
        <!--begin::Menu-->
        <button
          type="button"
          class="btn btn-sm btn-icon btn-color-primary btn-active-light-primary"
          data-kt-menu-trigger="click"
          data-kt-menu-placement="bottom-end"
          data-kt-menu-flip="top-end"
        >
          <KTIcon icon-name="category" icon-class="fs-2" />
        </button>
        <Dropdown2></Dropdown2>
        <!--end::Menu-->
      </div>
    </div>
    <!--end::Header-->

    <!--begin::Body Table-->
    <div class="card-body py-3">
      <!--begin::Table container-->
      <div class="table-responsive">
        <!--begin::Table-->
        <table
          class="table table-row-bordered table-row-gray-100 align-middle gs-0 gy-3"
        >
          <!--begin::Table head-->
          <thead>
            <tr class="fw-bold text-muted">
              <th class="w-25px">
                <div
                  class="form-check form-check-sm form-check-custom form-check-solid"
                >
                  <input
                    class="form-check-input"
                    type="checkbox"
                    @change="
                      checkedRows.length === 6
                        ? (checkedRows.length = 0)
                        : (checkedRows = [0, 1, 2, 3, 4, 5])
                    "
                  />
                </div>
              </th>
              <template v-for="header in tableHeader">
                <th>
                  {{ header.text }}
                </th>
              </template>




              <!-- <th class="min-w-150px">Order Id</th>
              <th class="min-w-140px">Country</th>
              <th class="min-w-120px">Date</th>
              <th class="min-w-120px">Company</th>
              <th class="min-w-120px">Total</th>
              <th class="min-w-120px">Status</th>
              <th class="min-w-100px text-end">Actions</th> -->
            </tr>
          </thead>
          <!--end::Table head-->

          <!--begin::Table body-->
          <tbody>
            <template v-for="(item, index) in tableData" >
              <tr>
                <td>
                  <div
                    class="form-check form-check-sm form-check-custom form-check-solid"
                  >
                    <input
                      class="form-check-input widget-13-check"
                      type="checkbox"
                      :value="index"
                      v-model="checkedRows"
                    />
                  </div>
                </td>

                <td>
                  <a
                    href="#"
                    class="text-dark fw-bold text-hover-primary d-block mb-1 fs-6"
                    >{{ item.projectName }}</a
                  >
                  <span class="text-muted fw-semobold text-muted d-block fs-7"
                    >{{ item.projectDescription }}</span
                  >
                </td>

                <td>
                  <a
                    href="#"
                    class="text-dark fw-bold text-hover-primary fs-6"
                    >{{ item.partner }}</a
                  >
                </td>

                <td>
                  <a
                    href="#"
                    class="text-dark fw-bold text-hover-primary fs-6"
                    >{{ item.manager }}</a
                  >
                </td>

                <td class="text-dark fw-bold fs-6"
                    >{{ item.startDate }}
                </td>

                <td class="text-dark fw-bold fs-6"
                    >{{ item.dueDate }}
                </td>
                <td class="text-dark fw-bold fs-6"
                    >{{ item.budget }}
                </td>
                
                <td>
                  <span
                    :class="`badge-light-${item.status}`"
                    class="badge"
                    >{{ item.status }}</span
                  >
                </td>

                <td class="text-end">
                  <a
                    href="#"
                    class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1"
                  >
                    <KTIcon icon-name="switch" icon-class="fs-3" />
                  </a>

                  <a
                    href="#"
                    class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1"
                  >
                    <KTIcon icon-name="pencil" icon-class="fs-3" />
                  </a>

                  <a
                    href="#"
                    class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm"
                  >
                    <KTIcon icon-name="trash" icon-class="fs-3" />
                  </a>
                </td>
              </tr>
            </template>
          </tbody>
          <!--end::Table body-->
        </table>
        <!--end::Table-->
      </div>
      <!--end::Table container-->
    </div>
    <!--end::Body-->
  </div>
  <!--end::Tables Widget 13-->

  <!--begin::Pagination-->
  <div class="d-flex flex-stack flex-wrap pt-10">
    <div class="fs-6 fw-semobold text-gray-700">
      Showing 1 to 10 of {{ tableData.length }} entries
    </div>

    <!--begin::Pages-->
    <ul class="pagination">
      <li class="page-item previous">
        <a href="#" class="page-link"><i class="previous"></i></a>
      </li>

      <li class="page-item active">
        <a href="#" class="page-link">1</a>
      </li>

      <li class="page-item">
        <a href="#" class="page-link">2</a>
      </li>

      <li class="page-item">
        <a href="#" class="page-link">3</a>
      </li>

      <li class="page-item">
        <a href="#" class="page-link">4</a>
      </li>

      <li class="page-item">
        <a href="#" class="page-link">5</a>
      </li>

      <li class="page-item">
        <a href="#" class="page-link">6</a>
      </li>

      <li class="page-item next">
        <a href="#" class="page-link"><i class="next"></i></a>
      </li>
    </ul>
    <!--end::Pages-->
  </div>
  <!--end::Pagination-->

</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, ref } from "vue";
import Dropdown2 from "@/components/dropdown/Dropdown2.vue";
import type { PropType } from 'vue';

type TableHeaderType = {
  text: string;
  value: string;
};
type TableDataType = {
  projectName: String,
  projectDescription: String,
  partner: String,
  manager:String,
  startDate:String,
  dueDate:String,
  budget:Number,
  status: String
};

export default defineComponent({
  name: "kt-widget-12",
  components: {
    Dropdown2,
  },

  props: {
    widgetClasses: String,
    tableHeader: {
      type: Array as PropType<TableHeaderType[]>,
      required: true,
    },
    tableData: {
      type: Array as PropType<TableDataType[]>,
      required: true,
    }
  },

  setup(props) {
    const checkedRows = ref<Array<number>>([]);
    return {
      checkedRows,
      getAssetPath,
      props,
    };
  },
});
</script>
