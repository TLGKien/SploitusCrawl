<template>
  <div
    class="modal fade"
    id="kt_modal_view_project"
    ref="viewProjectModalRef"
    tabindex="-1"
    aria-hidden="true"
  >
    <!--begin::Modal dialog-->
    <div class="modal-dialog modal-dialog-centered mw-650px">
      <!--begin::Modal content-->
      <div class="modal-content">
        <!--begin::Modal header-->
        <div class="modal-header" id="kt_modal_view_project_header">
          <!--begin::Modal title-->
          <h2 class="fw-bold">Cập nhật dự án</h2>
          <!--end::Modal title-->

          <!--begin::Close-->
          <div
            id="kt_modal_view_project_close"
            data-bs-dismiss="modal"
            class="btn btn-icon btn-sm btn-active-icon-primary"
          >
            <KTIcon icon-name="cross" icon-class="fs-1" />
          </div>
          <!--end::Close-->
        </div>
        <!--end::Modal header-->
        <!--begin::Form-->
        <el-form
          :model="formData"
          :rules="rules"
          ref="formRef"
        >
          <!--begin::Modal body-->
          <div class="modal-body py-10 px-lg-17">
            <!--begin::Scroll-->
            <div
              class="scroll-y me-n7 pe-7"
              id="kt_modal_view_project_scroll"
              data-kt-scroll="true"
              data-kt-scroll-activate="{default: false, lg: true}"
              data-kt-scroll-max-height="auto"
              data-kt-scroll-dependencies="#kt_modal_view_project_header"
              data-kt-scroll-wrappers="#kt_modal_view_project_scroll"
              data-kt-scroll-offset="300px"
            >
              <!--begin::Input group-->
              <div class="fv-row mb-7">
                <!--begin::Label-->
                <label class="required fs-6 fw-semobold mb-2">Mã dự án
                </label>
                <i
                    class="fas fa-exclamation-circle ms-1 fs-7"
                    data-bs-toggle="tooltip"
                    title="Mã dự án là duy nhất"
                  ></i>
                <!--end::Label-->
                

                <!--begin::Input-->
                <el-form-item prop="projectName">
                  <el-input 
                    v-model="formData.projectName" 
                    type="text" 
                    placeholder="" 
                    :disabled="true" 
                  />
                </el-form-item>
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="fv-row mb-7">
                <!--begin::Label-->
                <label class="fs-6 fw-semobold mb-2">Mô tả</label>
                <!--end::Label-->

                <!--begin::Input-->
                <el-form-item prop="projectDescription">
                  <el-input 
                    v-model="formData.projectDescription" 
                    type="text" 
                    placeholder=""
                    :disabled="true" 
                  />
                </el-form-item>
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="fv-row mb-7">
                <!--begin::Label-->
                <label class="fs-6 fw-semobold mb-2">Đối tác</label>
                <!--end::Label-->

                <!--begin::Input-->
                <el-form-item prop="partner">
                  <el-input 
                    v-model="formData.partner" 
                    type="text" 
                    placeholder=""
                    :disabled="true" 
                  />
                </el-form-item>
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="fv-row mb-7">
                <!--begin::Label-->
                <label class="fs-6 fw-semobold mb-2">Người phụ trách</label>
                <!--end::Label-->

                <!--begin::Input-->
                <el-form-item prop="manager">
                  <el-input 
                    v-model="formData.manager" 
                    type="text" 
                    placeholder=""
                    :disabled="true" 
                  />
                </el-form-item>
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="row g-9 mb-7">
                <!--begin::Col-->
                <div class="col-md-6 fv-row">
                  <!--begin::Label-->
                  <label class="fs-6 fw-semobold mb-2"
                    >Ngày bắt đầu</label
                  >
                  <!--end::Label-->

                  <!--begin::Input-->
                  <el-form-item prop="startDate">
                    <el-input 
                      v-model="formData.startDate" 
                      type="date" 
                      placeholder=""
                      :disabled="true" 
                    />
                  </el-form-item>
                  <!--end::Input-->
                </div>
                <!--end::Col-->

                <!--begin::Col-->
                <div class="col-md-6 fv-row">
                  <!--begin::Label-->
                  <label class="fs-6 fw-semobold mb-2"
                    >Ngày hết hạn</label
                  >
                  <!--end::Label-->

                  <!--begin::Input-->
                  <el-form-item prop="dueDate">
                    <el-input 
                      v-model="formData.dueDate" 
                      type="date" 
                      placeholder="" 
                      :disabled="true" 
                    />
                  </el-form-item>
                  <!--end::Input-->
                </div>
                <!--end::Col-->
              </div>

              <!--begin::Input group-->
              <div class="fv-row mb-7">
                <!--begin::Label-->
                <label class="fs-6 fw-semobold mb-2">Ngân sách</label>
                <!--end::Label-->
                <i
                  class="fas fa-exclamation-circle ms-1 fs-7"
                  data-bs-toggle="tooltip"
                  title="Tính theo đơn vị USD"
                ></i>

                <!--begin::Input-->
                <el-form-item prop="budget">
                  <el-input 
                    v-model="formData.budget" 
                    type="text" 
                    placeholder=""
                    :disabled="true" 
                  />
                </el-form-item>
                <!--end::Input-->
              </div>
              <!--end::Input group-->

              <!--begin::Input group-->
              <div class="fv-row mb-7">
                <!--begin::Label-->
                <label class="fs-6 fw-semobold mb-2">Trạng thái</label>
                <!--end::Label-->

                <!--begin::Input-->
                <el-select v-model="formData.status" class="el-input" :disabled="true" >
                  <el-option
                    v-for="(item, i) in statuses"
                    :key="`statuses-select-option-${i}`"
                    :value="item.status"
                  >
                    {{ item.status }}
                  </el-option>
                </el-select>

                <!--end::Input-->
              </div>
              <!--end::Input group-->
            </div>

            <!--end::Scroll-->
          </div>
          <!--end::Modal body-->

        </el-form>
        <!--end::Form-->
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, onMounted, ref, watch } from "vue";
import ApiService from "@/core/services/ApiService";

export default defineComponent({
  name: "view-project-modal",
  components: {},
  props: {
    pkSelected: { type: String, required: false, default: "" },
  },
  setup(props) {
    const formRef = ref<null | HTMLFormElement>(null);
    const viewProjectModalRef = ref<null | HTMLElement>(null);
    const loading = ref<boolean>(false);

    const formData = ref({
      pk: "",
      projectName: "",
      projectDescription: "",
      partner: "",
      manager: "",
      startDate: "",
      dueDate: "",
      budget: "",
      status: "Chờ xét duyệt",
    });
    const statuses = ref([
      {status: "Chờ xét duyệt", value:"pending"},
      {status: "Được chấp thuận", value:"approved"},
      {status: "Bị từ chối", value:"rejected"},
      {status: "Đã hoàn thành", value:"done"},
    ]);

    const rules = ref({
      projectName: [
        {
          required: true,
          message: "Tên dự án bắt buộc",
          trigger: "change",
        },
      ],
    });

    watch(() => props.pkSelected, (newData, oldData) => {
      LoadProject(newData);
    });

    const LoadProject = async (pkSelected) => {
      await ApiService.get(`project/${pkSelected}`)
       .then((response) => {
        formData.value = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
    }

    return {
      formData,
      rules,
      formRef,
      loading,
      viewProjectModalRef,
      getAssetPath,
      statuses,
    };
  },
});
</script>
