import bpy
import bpy_extras

class LogViewport(bpy.types.Menu):
    bl_label = "Log Viewport"
    bl_idname = "log_viewport"
    def draw(self, context):
        layout = self.layout
        layout.label(bpy.context.window.screen.show_fullscreen)


class MyViewport(bpy.types.Operator):
    bl_idname = "tools.logviewport"
    bl_label = "Display viewport data"
    answer = bpy.props.BoolProperty(name="Yes I want to select it.")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.label(bpy_extras.view3d_utils.region_2d_to_vector_3d(bpy.context.region, bpy.context.space_data.region_3d, (event.mouse_region_x, event.mouse_region_y)))
        layout.prop(self, "answer")
        pass


    def execute(self, context):
        bpy.ops.wm.call_menu(name=QuestionSelectNo.bl_idname)
        return {'FINISHED'}


bpy.utils.register_class(MyViewport)
bpy.utils.register_class(LogViewport)
