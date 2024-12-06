#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Hand_glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0
                            7.5
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    3.70000005
                }
                emitterName: string = "Flash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 0.570000768, 0.659998477 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.155930012
                            0.202203497
                            0.65456903
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.669993162, 0, 0 }
                            { 1, 0, 0, 1 }
                            { 0.908511579, 0, 0, 1 }
                            { 0.621192455, 0, 0, 0.289855063 }
                            { 0.333333343, 0, 0, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 120, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.5, 1 }
                            { 2, 8, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Illaoi/Skins/Base/Particles/Illaoi_Base_R_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            50
                            75
                        }
                    }
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
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.5
                            0.349999994
                        }
                    }
                }
                lifetime: option[f32] = {
                    3.5
                }
                emitterName: string = "Temp_Mesh"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_W_core_sphere.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
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
                pass: i16 = 1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_R_revive_energy.dds"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    45
                                    -45
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.232047826
                            0.570308685
                            1
                        }
                        values: list[vec3] = {
                            { 0.180000007, 1, 1 }
                            { 0.300000012, 0.767952144, 0.767952144 }
                            { 0.600000024, 0.429691315, 0.429691315 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_R_revive_energy.dds"
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 1.5 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 4, 1 }
            }
        }
        particleName: string = "Aatrox_Base_Recall_Hand_glow"
        particlePath: string = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Hand_glow"
    }
    "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Weapon_glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0
                            7.5
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                lifetime: option[f32] = {
                    3.70000005
                }
                emitterName: string = "Flash"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 0.570000768, 0.659998477 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.155930012
                            0.202203497
                            0.65456903
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.669993162, 0, 0 }
                            { 1, 0, 0, 1 }
                            { 0.908511579, 0, 0, 1 }
                            { 0.621192455, 0, 0, 0.289855063 }
                            { 0.333333343, 0, 0, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 120, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.5, 1 }
                            { 2, 8, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Illaoi/Skins/Base/Particles/Illaoi_Base_R_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            50
                            75
                        }
                    }
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
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.5
                            0.349999994
                        }
                    }
                }
                lifetime: option[f32] = {
                    3.5
                }
                emitterName: string = "Temp_Mesh"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_W_core_sphere.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
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
                pass: i16 = 1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_R_revive_energy.dds"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    45
                                    -45
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.232047826
                            0.570308685
                            1
                        }
                        values: list[vec3] = {
                            { 0.180000007, 1, 1 }
                            { 0.300000012, 0.767952144, 0.767952144 }
                            { 0.600000024, 0.429691315, 0.429691315 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_R_revive_energy.dds"
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 1.5 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 4, 1 }
            }
        }
        particleName: string = "Aatrox_Base_Recall_Weapon_glow"
        particlePath: string = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Weapon_glow"
    }
    "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Beam" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                lifetime: option[f32] = {
                    3
                }
                emitterName: string = "Chain"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveBeam {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_Recall_beam.scb"
                    }
                    mBeam: embed = VfxBeamDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 0, 150, 1 }
                            dynamics: pointer = VfxAnimatedVector3fVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {}
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            1
                                            1.20000005
                                        }
                                    }
                                    VfxProbabilityTableData {}
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[vec3] = {
                                    { 0, 150, 1 }
                                }
                            }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.65882355, 0.0509803928, 0.0509803928, 1 }
                            { 1, 0, 0, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                1
                                0.600000024
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_R_Thresh_Skin05_R_Einstein_01_mult.dds"
                }
                birthRotation0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 555, 550, 550 }
                }
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_R_revive_blood.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 4, 2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 4, 2 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                            { 2, 0 }
                        }
                    }
                }
            }
        }
        particleName: string = "Aatrox_Base_Recall_Beam"
        particlePath: string = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Beam"
    }
}
