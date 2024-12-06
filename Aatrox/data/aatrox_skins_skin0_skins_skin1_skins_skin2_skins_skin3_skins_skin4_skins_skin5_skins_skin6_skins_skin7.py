#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Dash_trail" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterLinger: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Temp_Trail"
                disabled: bool = true
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 50, -50 }
                }
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.333333343, 0, 0.498039216, 0 }
                            { 0.525490224, 0, 0.121568628, 0.501960814 }
                            { 0.333333343, 0, 0, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_E_TEMP_trail.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterLinger: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Temp_Trail1"
                disabled: bool = true
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 50, -50 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.333333343, 0, 0.498039216, 0 }
                            { 0.525490224, 0.172549024, 0, 0.501960814 }
                            { 0.333333343, 0, 0, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 200, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_E_TEMP_trail.dds"
            }
        }
        particleName: string = "Aatrox_Base_E_Dash_trail"
        particlePath: string = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Dash_trail"
    }
}
