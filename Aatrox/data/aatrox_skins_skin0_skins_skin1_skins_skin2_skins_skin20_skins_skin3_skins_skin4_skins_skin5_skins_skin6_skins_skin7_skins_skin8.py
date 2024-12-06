#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_P_Debuff" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "symbol"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 130, -50 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Global_Debuff_AMPen_Shield_Glow.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1000
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 0.699999988, 0.699999988 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.0700000003
                            0.100000001
                            0.119999997
                            0.140000001
                            0.150000006
                            0.180000007
                            0.300000012
                            0.319999993
                            0.340000004
                            0.349999994
                            0.379999995
                            0.5
                            0.519999981
                            0.540000021
                            0.550000012
                            0.579999983
                            0.699999988
                            0.720000029
                            0.74000001
                            0.75
                            0.779999971
                            0.899999976
                            0.920000017
                            0.939999998
                            0.949999988
                            0.980000019
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.10000002, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.25, 1, 1 }
                            { 1, 1, 1 }
                            { 1.14999998, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.25, 1, 1 }
                            { 1, 1, 1 }
                            { 1.14999998, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.25, 1, 1 }
                            { 1, 1, 1 }
                            { 1.14999998, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.25, 1, 1 }
                            { 1, 1, 1 }
                            { 1.14999998, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.25, 1, 1 }
                            { 1, 1, 1 }
                            { 1.14999998, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_Passive_Debuff_symbol.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.75
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "SoftBeams"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 120, -50 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0, 0, 0.349019617 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0, 0 }
                            { 1, 0, 0, 0.349019617 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500100017
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0
                                    -45
                                    -135
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0
                                    -180
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 8, 3, 0 }
                            { 3, 5, 0 }
                            { 0, 7, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Global_Debuff_AMPen_SoftRays_4x1.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    2.79999995
                }
                emitterName: string = "Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 145, -50 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.466666669, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 160, 160 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Global_Debuff_AMPen_Glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "spawn2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 125, -50 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Global_Debuff_AMPen_Shield_Glow.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 0.454901963, 0.454901963, 0.831372559 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1003
                miscRenderFlags: u8 = 1
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 35 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 0.200000003, 1 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.10000002, 1 }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_P_debuff_icon_slash.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_P_debuff_mult.dds"
                    texAddressModeMult: u8 = 2
                    uvScrollClampMult: flag = true
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 6, 0 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { -1, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "spawn3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 139, -53 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Global_Debuff_AMPen_Shield_Glow.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 0.396078438, 0.396078438, 0.933333337 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1002
                miscRenderFlags: u8 = 1
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 148 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0.300000012, 1 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.10000002, 1 }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_P_debuff_icon_slash.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_P_debuff_mult.dds"
                    texAddressModeMult: u8 = 2
                    uvScrollClampMult: flag = true
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 6, 0 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { -1, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "spawn1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 130, -50 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Global_Debuff_AMPen_Shield_Glow.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.949996173 }
                            { 1, 0.37000075, 0.179995418, 0.730006874 }
                            { 0.933333337, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1001
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 0.699999988, 0.699999988 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.0700000003
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.10000002, 1, 1 }
                            { 1.10000002, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_Passive_Debuff_symbol_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.9000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "symbol1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 130, -50 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Global_Debuff_AMPen_Shield_Glow.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 999
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1.10000002, 1.10000002 }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_Passive_Debuff_symbol02.dds"
            }
        }
        particleName: string = "Aatrox_Base_P_Debuff"
        particlePath: string = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_P_Debuff"
    }
}
