# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dti import VecReg


def test_VecReg_inputs():
    input_map = dict(
        affine_mat=dict(argstr="-t %s", extensions=None,),
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="-i %s", extensions=None, mandatory=True,),
        interpolation=dict(argstr="--interp=%s",),
        mask=dict(argstr="-m %s", extensions=None,),
        out_file=dict(argstr="-o %s", extensions=None, genfile=True, hash_files=False,),
        output_type=dict(),
        ref_mask=dict(argstr="--refmask=%s", extensions=None,),
        ref_vol=dict(argstr="-r %s", extensions=None, mandatory=True,),
        rotation_mat=dict(argstr="--rotmat=%s", extensions=None,),
        rotation_warp=dict(argstr="--rotwarp=%s", extensions=None,),
        warp_field=dict(argstr="-w %s", extensions=None,),
    )
    inputs = VecReg.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_VecReg_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = VecReg.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
