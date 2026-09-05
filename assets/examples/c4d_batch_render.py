# C4D Python 批量渲染脚本模板
# 用途：遍历场景中的相机并分别渲染
# 使用：在C4D脚本管理器中运行（Script → Script Manager）

import c4d
from c4d import documents

def main():
    doc = documents.GetActiveDocument()

    # 获取所有相机
    cameras = []
    def find_cameras(obj):
        if obj is None:
            return
        if obj.GetType() == c4d.Ocamera:
            cameras.append(obj)
        find_cameras(obj.GetDown())
        find_cameras(obj.GetNext())

    find_cameras(doc.GetFirstObject())

    if not cameras:
        print("未找到相机对象")
        return

    # 渲染设置
    renderData = doc.GetActiveRenderData()
    renderData[c4d.RDATA_FORMAT] = c4d.FILTER_PNG
    renderData[c4d.RDATA_XRES] = 3000
    renderData[c4d.RDATA_YRES] = 2000

    # 渲染输出目录
    output_dir = "C:/Renders/"

    # 逐相机渲染
    for i, cam in enumerate(cameras):
        doc.SetActiveRenderCam(cam)

        filename = f"{output_dir}camera_{i:02d}_{cam.GetName()}.png"
        renderData[c4d.RDATA_PATH] = filename

        bmp = c4d.bitmaps.BaseBitmap()
        bmp.Init(renderData[c4d.RDATA_XRES], renderData[c4d.RDATA_YRES])

        result = documents.RenderDocument(
            doc, renderData.GetData(), bmp,
            c4d.RENDERFLAGS_EXTERNAL
        )

        if result == c4d.RENDERRESULT_OK:
            bmp.Save(filename, c4d.FILTER_PNG)
            print(f"Rendered: {filename}")
        else:
            print(f"Failed: {cam.GetName()}")

        bmp.FlushAll()

    print(f"Done! Rendered {len(cameras)} views")

if __name__ == '__main__':
    main()
