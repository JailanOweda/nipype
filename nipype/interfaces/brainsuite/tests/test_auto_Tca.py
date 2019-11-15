# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brainsuite import Tca


def test_Tca_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        foregroundDelta=dict(argstr="--delta %d", usedefault=True,),
        inputMaskFile=dict(argstr="-i %s", extensions=None, mandatory=True,),
        maxCorrectionSize=dict(argstr="-n %d",),
        minCorrectionSize=dict(argstr="-m %d", usedefault=True,),
        outputMaskFile=dict(argstr="-o %s", extensions=None, genfile=True,),
        timer=dict(argstr="--timer",),
        verbosity=dict(argstr="-v %d",),
    )
    inputs = Tca.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Tca_outputs():
    output_map = dict(outputMaskFile=dict(extensions=None,),)
    outputs = Tca.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
