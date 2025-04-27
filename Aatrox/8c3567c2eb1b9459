#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Core_End" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundLines_erode"
                Filtering: pointer = VfxEmitterFiltering {
                    spectatorPolicy: u8 = 1
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            0.610000014
                            1
                        }
                        values: list[f32] = {
                            1
                            1
                            0
                            0
                        }
                    }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 1, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_W_Ground_fade.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.250003815, 0.11999695, 0.11999695, 0.500007629 }
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
                pass: i16 = -3
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 2
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                2
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_Q_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 540, 600, 1 }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_W_indicator.dds"
            }
        }
        particleName: string = "Aatrox_Base_W_Core_End"
        particlePath: string = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Core_End"
    }
}
