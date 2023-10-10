<template>
  <div
    class="modal fade"
    id="kt_modal_delete_project"
    ref="deleteProjectModalRef"
    tabindex="-1"
    aria-hidden="true"
  >
    <!--begin::Modal dialog-->
    <div class="modal-dialog modal-dialog-centered mw-650px">
      <!--begin::Modal content-->
      <div class="modal-content">
        <!--begin::Modal header-->
        <div class="modal-header" id="kt_modal_delete_project_header">
          <!--begin::Modal title-->
          <h2 class="fw-bold">Xác nhận xóa dự án {{ formData.projectName }} - {{ formData.projectDescription }}</h2>
          <!--end::Modal title-->

          <!--begin::Close-->
          <div
            id="kt_modal_delete_project_close"
            data-bs-dismiss="modal"
            class="btn btn-icon btn-sm btn-active-icon-primary"
          >
            <KTIcon icon-name="cross" icon-class="fs-1" />
          </div>
          <!--end::Close-->
        </div>
        <!--end::Modal header-->

        
          <div class="modal-footer flex-center">
            <!--begin::Button-->
            <button
              type="button"
              id="kt_modal_delete_project_cancel"
              class="btn btn-light me-3"
              @click="cancelClick()"
            >
              Hủy
            </button>
            <!--end::Button-->

            <!--begin::Button-->
            <button
              :data-kt-indicator="loading ? 'on' : null"
              class="btn btn-lg btn-primary"
              type="button"
              @click="deleteClick()"
            >
              <span v-if="!loading" class="indicator-label">
                Xóa
              </span>
              <span v-if="loading" class="indicator-progress">
                Đang xử lý...
                <span
                  class="spinner-border spinner-border-sm align-middle ms-2"
                ></span>
              </span>
            </button>
            <!--end::Button-->
          </div>

      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { getAssetPath } from "@/core/helpers/assets";
import { defineComponent, onMounted, ref, watch } from "vue";
import { hideModal } from "@/core/helpers/dom";
import Swal from "sweetalert2/dist/sweetalert2.js";
import ApiService from "@/core/services/ApiService";
// import { useAuthStore} from "@/stores/auth";
// import Cookies from 'js-cookie'; 

export default defineComponent({
  name: "delete-project-modal",
  components: {},
  props: {
    pkSelected: { type: String, required: false, default: "" },
  },
  emits: ["on-refresh"],
  setup(props, { emit }) {
    const formRef = ref<null | HTMLFormElement>(null);
    const deleteProjectModalRef = ref<null | HTMLElement>(null);
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

    const cancelClick = () => {
      hideModal(deleteProjectModalRef.value);
    };

    const deleteClick = async () => {
      loading.value = true;
      // gửi request
      await ApiService.delete(`project/delete/${formData.value.pk}/`)
      .then((response) => {
        console.log(response);
        setTimeout(() => {
          loading.value = false;

          Swal.fire({
            text: "Đã xóa!",
            icon: "success",
            buttonsStyling: false,
            confirmButtonText: "Ok",
            heightAuto: true,
            customClass: {
              confirmButton: "btn btn-primary",
            },
          }).then(() => {
            hideModal(deleteProjectModalRef.value);
            emit('on-refresh');
          });
        }, 2000);
      })
      .catch((error) => {
        console.error(error);
        Swal.fire({
          text: "Sorry, looks like there are some errors detected, please try again.",
          icon: "error",
          buttonsStyling: false,
          confirmButtonText: "Ok",
          heightAuto: false,
          customClass: {
            confirmButton: "btn btn-primary",
          },
        });
        return false;
      });
    };

    watch(() => props.pkSelected, (newData, oldData) => {
      LoadProject(newData);
    });

    const LoadProject = async (pkSelected) => {
      await ApiService.get("project/"+pkSelected)
       .then((response) => {
        formData.value = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
    }

    return {
      formData,
      formRef,
      loading,
      deleteProjectModalRef,
      getAssetPath,
      cancelClick,
      deleteClick,
    };
  },
});
</script>
