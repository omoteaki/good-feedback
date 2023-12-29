# sessionを使わない方法にしたのでなし
# class CreateProjectSuccessView(ListView):
#     template_name = "new_project.html"
# 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["new_project"] = self.request.session["form_project"]
#         return context
# 
# sessionを使うことを考える前には、登録ユーザーの中で一番pkが大きいプロジェクトを取ろうとしていた
#     def get_queryset(self):
#         print(self.request.user)
#         new_project_id = Project.objects.filter(created_user = self.kwargs["created_user_id"]).aggregate(Max("id"))
#         new_project = Project.objects.get(id=new_project_id["id__max"])
#         return new_project


# class CreateProjectView(CreateView):
# 
#     def form_valid(self, form):
# 
#         '''
#         sessionで次のページに登録情報を渡そうとしたけど、
#         save() & super().form_valid(form)の後でself.objectで保存したデータを取得できる
#         '''
#         # project_data = form.cleaned_data
#         # project_data["deadline_datetime"] = ""
#         # project_data["contractor_user"] = ""
#         # if not 'form_project' in self.request.session:
#         #     self.request.session['form_project'] = project_data