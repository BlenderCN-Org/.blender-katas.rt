import bpy


class QuestionSelectYes(bpy.types.Menu):
	bl_label = "Question For Selection"
	bl_idname = "question_select_yes"
	def draw(self, context):
		layout = self.layout
		layout.label("You selected it...")


class QuestionSelectNo(bpy.types.Menu):
	bl_label = "Question For Selection"
	bl_idname = "question_select_no"
	def draw(self, context):
		layout = self.layout
		layout.label("You didn't select it...")


class Question(bpy.types.Operator):
	bl_idname = "tools.question"
	bl_label = "Question For Selection"
	answer = bpy.props.BoolProperty(name="Yes I want to select it.")


	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)


	def draw(self, context):
		layout = self.layout
		layout.label("Are you really sure you want to select it?")
		layout.prop(self, "answer")
		pass


	def execute(self, context):
		if self.answer:
			bpy.ops.wm.call_menu(name=QuestionSelectYes.bl_idname)
		else:
			bpy.ops.wm.call_menu(name=QuestionSelectNo.bl_idname)
		return {'FINISHED'}


bpy.utils.register_class(Question)
bpy.utils.register_class(QuestionSelectYes)
bpy.utils.register_class(QuestionSelectNo)
