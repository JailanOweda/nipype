# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import MedianFilter3D


def test_MedianFilter3D_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        debug=dict(argstr="-debug", position=1,),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2,),
        out_filename=dict(argstr="%s", extensions=None, genfile=True, position=-1,),
        quiet=dict(argstr="-quiet", position=1,),
    )
    inputs = MedianFilter3D.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MedianFilter3D_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = MedianFilter3D.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
