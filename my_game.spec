# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['play_game.py'],
    pathex=["E:\\code\\alien"],
    binaries=[],
    datas=[
        ('image', 'image'),  # 将'image'文件夹添加到datas
        ('sound', 'sound')   # 将'sound'文件夹添加到datas
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='my_game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 如果你需要控制台窗口，将此值设为True
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='my_game',
)
