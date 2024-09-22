#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Aatrox_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/Aatrox/Aatrox.bin"
    "DATA/Aatrox_Skins_Skin0_Skins_Skin2_Skins_Skin20_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8.bin"
    "DATA/Characters/Aatrox/Animations/Skin0.bin"
    "DATA/Aatrox_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin2_Skins_Skin20_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Aatrox_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7.bin"
    "DATA/Aatrox_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin20_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8.bin"
    "DATA/Aatrox_Skins_Skin0_Skins_Skin2_Skins_Skin20_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8.bin"
    "DATA/Aatrox_Skins_Skin0_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6.bin"
    "DATA/Aatrox_Skins_Skin0_Skins_Skin1_Skins_Skin3.bin"
    "DATA/Aatrox_Skins_Skin0_Skins_Skin3_Skins_Skin7.bin"
    "DATA/Aatrox_Skins_Skin0_Skins_Skin3.bin"
}
entries: map[hash,embed] = {
    "Characters/Aatrox/Skins/Skin0" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "Aatrox"
        metaDataTags: string = "gender:male,race:darkin,element:dark"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Aatrox/Skins/Base/AatroxLoadscreen.dds"
        }
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "Aatrox"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "Aatrox_Base_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Aatrox/Skins/Base/Aatrox_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Aatrox/Skins/Base/Aatrox_Base_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_Aatrox_AatroxBasicAttack2_OnCast"
                        "Play_sfx_Aatrox_AatroxBasicAttack2_OnHit"
                        "Play_sfx_Aatrox_AatroxBasicAttack3_OnCast"
                        "Play_sfx_Aatrox_AatroxBasicAttack3_OnHit"
                        "Play_sfx_Aatrox_AatroxBasicAttack_OnCast"
                        "Play_sfx_Aatrox_AatroxBasicAttack_OnHit"
                        "Play_sfx_Aatrox_AatroxCritAttack_OnCast"
                        "Play_sfx_Aatrox_AatroxCritAttack_OnHit"
                        "Play_sfx_Aatrox_AatroxE_OnCast"
                        "Play_sfx_Aatrox_AatroxPassiveAttack_OnCast"
                        "Play_sfx_Aatrox_AatroxPassiveAttack_OnHit"
                        "Play_sfx_Aatrox_AatroxPassiveDebuff_OnBuffActivate"
                        "Play_sfx_Aatrox_AatroxPassiveDebuff_OnBuffDeactivate"
                        "Play_sfx_Aatrox_AatroxPassiveReady_OnBuffActivate"
                        "Play_sfx_Aatrox_AatroxQ1_OnCast_all"
                        "Play_sfx_Aatrox_AatroxQ1_OnHit_miss"
                        "Play_sfx_Aatrox_AatroxQ1_OnHit_normal_all"
                        "Play_sfx_Aatrox_AatroxQ1_OnHit_normal_player"
                        "Play_sfx_Aatrox_AatroxQ1_OnHit_sweetspot_all"
                        "Play_sfx_Aatrox_AatroxQ1_OnHit_sweetspot_player"
                        "Play_sfx_Aatrox_AatroxQ2_OnCast_all"
                        "Play_sfx_Aatrox_AatroxQ2_OnHit_miss"
                        "Play_sfx_Aatrox_AatroxQ2_OnHit_normal_all"
                        "Play_sfx_Aatrox_AatroxQ2_OnHit_normal_player"
                        "Play_sfx_Aatrox_AatroxQ2_OnHit_sweetspot_all"
                        "Play_sfx_Aatrox_AatroxQ2_OnHit_sweetspot_player"
                        "Play_sfx_Aatrox_AatroxQ3_OnCast_all"
                        "Play_sfx_Aatrox_AatroxQ3_OnHit_miss"
                        "Play_sfx_Aatrox_AatroxQ3_OnHit_normal_all"
                        "Play_sfx_Aatrox_AatroxQ3_OnHit_normal_player"
                        "Play_sfx_Aatrox_AatroxQ3_OnHit_sweetspot_all"
                        "Play_sfx_Aatrox_AatroxQ3_OnHit_sweetspot_player"
                        "Play_sfx_Aatrox_AatroxR_6seconds"
                        "Play_sfx_Aatrox_AatroxR_buffdeactivate"
                        "Play_sfx_Aatrox_AatroxR_end"
                        "Play_sfx_Aatrox_AatroxR_OnBuffActivate_all"
                        "Play_sfx_Aatrox_AatroxR_OnBuffActivate_player"
                        "Play_sfx_Aatrox_AatroxRAttack1_OnCast"
                        "Play_sfx_Aatrox_AatroxRAttack1_OnHit"
                        "Play_sfx_Aatrox_AatroxRAttack2_OnCast"
                        "Play_sfx_Aatrox_AatroxRAttack2_OnHit"
                        "Play_sfx_Aatrox_AatroxRRevive_all"
                        "Play_sfx_Aatrox_AatroxRRevive_player"
                        "Play_sfx_Aatrox_AatroxW_OnCast"
                        "Play_sfx_Aatrox_AatroxW_OnHit"
                        "Play_sfx_Aatrox_AatroxW_OnMissileCast"
                        "Play_sfx_Aatrox_AatroxW_OnMissileLaunch"
                        "Play_sfx_Aatrox_AatroxWBump_OnBuffActivate"
                        "Play_sfx_Aatrox_AatroxWChains_OnBuffActivate"
                        "Play_sfx_Aatrox_AatroxWChains_OnBuffDeactivate"
                        "Play_sfx_Aatrox_Dance3D_In_buffactivate"
                        "Play_sfx_Aatrox_Dance3D_loop_buffactivate"
                        "Play_sfx_Aatrox_Death3D_cast"
                        "Play_sfx_Aatrox_Joke3D_buffactivate"
                        "Play_sfx_Aatrox_Recall3D_buffactivate"
                        "Play_sfx_Aatrox_Taunt3D_buffactivate"
                        "Set_Switch_Aatrox_R_Active"
                        "Set_Switch_Aatrox_R_Inactive"
                        "Stop_sfx_Aatrox_AatroxW_OnMissileLaunch"
                        "Stop_sfx_Aatrox_AatroxWBump_OnBuffActivate"
                        "Stop_sfx_Aatrox_AatroxWChains_OnBuffActivate"
                        "Stop_sfx_Aatrox_Dance3D_In_buffactivate"
                        "Stop_sfx_Aatrox_Joke3D_buffactivate"
                        "Stop_sfx_Aatrox_Recall3D_buffactivate"
                        "Stop_sfx_Aatrox_Taunt3D_buffactivate"
                        "Switch_Aatrox_Footsteps_Brush"
                        "Switch_Aatrox_Footsteps_Dirt"
                        "Switch_Aatrox_Footsteps_Stone"
                        "Switch_Aatrox_Footsteps_Water"
                    }
                }
                BankUnit {
                    name: string = "Aatrox_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Aatrox/Skins/Base/Aatrox_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Aatrox/Skins/Base/Aatrox_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Aatrox/Skins/Base/Aatrox_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_Aatrox_AatroxE_cast3D"
                        "Play_vo_Aatrox_AatroxQ_OnCast"
                        "Play_vo_Aatrox_AatroxR_cast3D"
                        "Play_vo_Aatrox_AatroxRRevive_OnBuffCast"
                        "Play_vo_Aatrox_AatroxW_cast3D"
                        "Play_vo_Aatrox_Attack2DGeneral"
                        "Play_vo_Aatrox_Attack2DPantheon"
                        "Play_vo_Aatrox_Attack2DTryndamere"
                        "Play_vo_Aatrox_Attack2DZoe"
                        "Play_vo_Aatrox_Death3D"
                        "Play_vo_Aatrox_FirstEncounter3DAkali"
                        "Play_vo_Aatrox_FirstEncounter3DAnivia"
                        "Play_vo_Aatrox_FirstEncounter3DCamille"
                        "Play_vo_Aatrox_FirstEncounter3DDarius"
                        "Play_vo_Aatrox_FirstEncounter3DFiora"
                        "Play_vo_Aatrox_FirstEncounter3DGalio"
                        "Play_vo_Aatrox_FirstEncounter3DGangplank"
                        "Play_vo_Aatrox_FirstEncounter3DGaren"
                        "Play_vo_Aatrox_FirstEncounter3DGeneral"
                        "Play_vo_Aatrox_FirstEncounter3DIllaoi"
                        "Play_vo_Aatrox_FirstEncounter3DJax"
                        "Play_vo_Aatrox_FirstEncounter3DKaisa"
                        "Play_vo_Aatrox_FirstEncounter3DKayle"
                        "Play_vo_Aatrox_FirstEncounter3DKayn"
                        "Play_vo_Aatrox_FirstEncounter3DKennen"
                        "Play_vo_Aatrox_FirstEncounter3DKled"
                        "Play_vo_Aatrox_FirstEncounter3DMalphite"
                        "Play_vo_Aatrox_FirstEncounter3DMaokai"
                        "Play_vo_Aatrox_FirstEncounter3DMorgana"
                        "Play_vo_Aatrox_FirstEncounter3DMundo"
                        "Play_vo_Aatrox_FirstEncounter3DNasus"
                        "Play_vo_Aatrox_FirstEncounter3DNautilus"
                        "Play_vo_Aatrox_FirstEncounter3DOrnn"
                        "Play_vo_Aatrox_FirstEncounter3DPantheon"
                        "Play_vo_Aatrox_FirstEncounter3DQuinn"
                        "Play_vo_Aatrox_FirstEncounter3DRenekton"
                        "Play_vo_Aatrox_FirstEncounter3DRiven"
                        "Play_vo_Aatrox_FirstEncounter3DRumble"
                        "Play_vo_Aatrox_FirstEncounter3DShen"
                        "Play_vo_Aatrox_FirstEncounter3DSion"
                        "Play_vo_Aatrox_FirstEncounter3DTargon"
                        "Play_vo_Aatrox_FirstEncounter3DTaric"
                        "Play_vo_Aatrox_FirstEncounter3DTeemo"
                        "Play_vo_Aatrox_FirstEncounter3DTrundle"
                        "Play_vo_Aatrox_FirstEncounter3DTryndamere"
                        "Play_vo_Aatrox_FirstEncounter3DVarus"
                        "Play_vo_Aatrox_FirstEncounter3DVoid"
                        "Play_vo_Aatrox_FirstEncounter3DYorick"
                        "Play_vo_Aatrox_FirstEncounter3DZoe"
                        "Play_vo_Aatrox_Joke3DGeneral"
                        "Play_vo_Aatrox_Kill3DAatrox"
                        "Play_vo_Aatrox_Kill3DAnivia"
                        "Play_vo_Aatrox_Kill3DCamille"
                        "Play_vo_Aatrox_Kill3DDarius"
                        "Play_vo_Aatrox_Kill3DFiora"
                        "Play_vo_Aatrox_Kill3DGangplank"
                        "Play_vo_Aatrox_Kill3DGaren"
                        "Play_vo_Aatrox_Kill3DGeneral"
                        "Play_vo_Aatrox_Kill3DIllaoi"
                        "Play_vo_Aatrox_Kill3DKaisa"
                        "Play_vo_Aatrox_Kill3DKayle"
                        "Play_vo_Aatrox_Kill3DKayn"
                        "Play_vo_Aatrox_Kill3DKled"
                        "Play_vo_Aatrox_Kill3DMalphite"
                        "Play_vo_Aatrox_Kill3DMaokai"
                        "Play_vo_Aatrox_Kill3DMorgana"
                        "Play_vo_Aatrox_Kill3DNasus"
                        "Play_vo_Aatrox_Kill3DNautilus"
                        "Play_vo_Aatrox_Kill3DOrnn"
                        "Play_vo_Aatrox_Kill3DPantheon"
                        "Play_vo_Aatrox_Kill3DRiven"
                        "Play_vo_Aatrox_Kill3DShen"
                        "Play_vo_Aatrox_Kill3DSion"
                        "Play_vo_Aatrox_Kill3DTaric"
                        "Play_vo_Aatrox_Kill3DTeemo"
                        "Play_vo_Aatrox_Kill3DTryndamere"
                        "Play_vo_Aatrox_Kill3DVarus"
                        "Play_vo_Aatrox_Kill3DZoe"
                        "Play_vo_Aatrox_Laugh3DGeneral"
                        "Play_vo_Aatrox_MasteryResponse3DGeneral"
                        "Play_vo_Aatrox_Move2DFirstPantheon"
                        "Play_vo_Aatrox_Move2DLong"
                        "Play_vo_Aatrox_Move2DRReady"
                        "Play_vo_Aatrox_Move2DStandard"
                        "Play_vo_Aatrox_Taunt3DGeneral"
                    }
                    voiceOver: bool = true
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Aatrox/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Aatrox/Skins/Base/Aatrox.skl"
            simpleSkin: string = "ASSETS/Characters/Aatrox/Skins/Base/Aatrox.skn"
            texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Aatrox_Base_TX_CM.dds"
            skinScale: f32 = 1.09000003
            selfIllumination: f32 = 0.699999988
            brushAlphaOverride: f32 = 0.550000012
            overrideBoundingBox: option[vec3] = {
                { 130, 250, 130 }
            }
            material: link = "Characters/Aatrox/Skins/Skin0/Materials/Aatrox_VFXBase_inst"
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Wings"
            initialSubmeshShadowsToHide: string = "Banner"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    material: link = "Characters/Aatrox/Skins/Skin0/Materials/Sword_inst"
                    submesh: string = "Sword"
                }
                SkinMeshDataProperties_MaterialOverride {
                    material: link = "Characters/Aatrox/Skins/Skin0/Materials/Wing_inst"
                    submesh: string = "Wings"
                }
                SkinMeshDataProperties_MaterialOverride {
                    material: link = "Characters/Aatrox/Skins/Skin0/Materials/Banner_inst"
                    submesh: string = "Banner"
                }
            }
            rigPoseModifierData: list[pointer] = {
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = "L_Wing_Banner_Ground1"
                    mEndingJointName: hash = "L_Wing_Banner_Ground4"
                    mDefaultMaskName: hash = "empty"
                    mMaxBoneAngle: f32 = 150
                    mVelMultiplier: f32 = 0
                    mFrequency: f32 = 5
                }
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = "R_Wing_Banner_Ground1"
                    mEndingJointName: hash = "R_Wing_Banner_Ground4"
                    mDefaultMaskName: hash = "empty"
                    mMaxBoneAngle: f32 = 150
                    mVelMultiplier: f32 = 0
                    mFrequency: f32 = 5
                }
            }
        }
        armorMaterial: string = "Flesh"
        defaultAnimations: list[string] = {
            "BaseBuffPose"
        }
        mContextualActionData: link = "Characters/Aatrox/CAC/Aatrox_Base"
        iconCircle: option[string] = {
            "ASSETS/Characters/Aatrox/HUD/Aatrox_Circle.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Aatrox/HUD/Aatrox_Square.dds"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            attachToBone: string = "Buffbone_Cstm_Healthbar"
            unitHealthBarStyle: u8 = 11
        }
        mResourceResolver: link = "Characters/Aatrox/Skins/Skin0/Resources"
        PersistentEffectConditions: list2[pointer] = {
            PersistentEffectConditionData {
                OwnerCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                    Spell: hash = "Characters/Aatrox/Spells/AatroxPassiveAbility/AatroxPassiveReady"
                }
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        boneName: string = "Weapon_Heart"
                        effectKey: hash = "Aatrox_P_Ready"
                    }
                }
            }
        }
    }
    "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Active_buff" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                            "Shoulder"
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
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
                depthBiasFactors: vec2 = { -1, -1 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00100005, 1.00100005, 1.00100005 }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_E_buff_avatar.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar_activate"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                            "Shoulder"
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.650003791 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.650003791 }
                            { 1, 1, 1, 0.650003791 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                uvScrollClamp: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1.00999999, 1.00999999 }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_E_buff_avatar_sheen.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 2 }
                }
                texAddressModeBase: u8 = 2
            }
        }
        particleName: string = "Aatrox_Base_E_Active_buff"
        particlePath: string = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Active_buff"
    }
    "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Dash" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    1.10000002
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 50 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.5
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_Q_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Aatrox_Base_TX_CM.dds"
                numFrames: u16 = 4
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    1.10000002
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 50 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Sword"
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Aatrox_Base_Sword_TX_CM.dds"
                numFrames: u16 = 4
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    1.10000002
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 50 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Wings"
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.5
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_Q_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Aatrox_Wings_TX_CM.dds"
                numFrames: u16 = 4
            }
        }
        particleName: string = "Aatrox_Base_E_Dash"
        particlePath: string = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Dash"
        mIsPoseAfterimage: bool = true
    }
    "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_P_Ready" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Basic"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.330006868, 0, 0, 1 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
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
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 100, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 100, 100 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.25, 0.25, 2.5 }
                            { 1, 1, 1 }
                            { 0.25, 0.25, 0.25 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_TEMP_Diana_Skin11_W_FaintGlow.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_AA_Gradient_RGB.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 8
                }
            }
        }
        particleName: string = "Aatrox_Base_P_Ready"
        particlePath: string = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_P_Ready"
    }
    "Characters/Aatrox/Skins/Skin0/Materials/Sword_inst" = StaticMaterialDef {
        name: string = "Characters/Aatrox/Skins/Skin0/Materials/Sword_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Characters/Aatrox/Skins/Base/Aatrox_Base_Sword_TX_CM.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_P_Sword_Mask.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Gradient_Texture"
                textureName: string = "ASSETS/Shared/Materials/Gradient_test_01.dds"
                addressU: u32 = 1
                addressV: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Mask_Intensity"
                value: vec4 = { 0.792500019, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 4, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scrolling_Scale"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scrolling_Rate"
                value: vec4 = { 0, -1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color"
                value: vec4 = { 1, 0.301960796, 0.0274509806, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dissolve_Bias"
                value: vec4 = { -1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dissolve_SmoothStep"
                value: vec4 = { 0, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Gradient_Sharpness"
                value: vec4 = { 0.400000006, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Sharpness"
                value: vec4 = { 0.00100000005, 0, 0, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_COLORDODGE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_ADDATIVE"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_LERP"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_DISSOLVE"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/SkinnedMesh/Scrolling_ColorDodge_Masked"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        childTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                name: string = "transition"
                parentName: string = "normal"
                shaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "Mask_Intensity"
                    driver: pointer = LerpMaterialDriver {
                        mBoolDriver: pointer = HasBuffDynamicMaterialBoolDriver {
                            mScriptName: string = "AatroxPassiveReady"
                        }
                        mOnValue: f32 = 0.75
                        mTurnOffTimeSec: f32 = 0.200000003
                    }
                }
            }
        }
    }
    "Characters/Aatrox/Skins/Skin0/Materials/Banner_inst" = StaticMaterialDef {
        name: string = "Characters/Aatrox/Skins/Skin0/Materials/Banner_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_I_Banner_color.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_I_Banner.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "UV_Scale"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed"
                value: vec4 = { 0, -0.300000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Bias"
                value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Scale_BLUE"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed_BLUE"
                value: vec4 = { 0, -0.200000003, 0, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "MULTIPLY_ADD"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_RED_TO_ALPHA"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_BLUE_CHANNEL"
            }
        }
        shaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/SkinnedMesh/ScrollingCustomAlpha"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        childTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                name: string = "transition"
                parentName: string = "normal"
                shaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
    }
    "Characters/Aatrox/Skins/Skin0/Materials/Aatrox_VFXBase_inst" = StaticMaterialDef {
        name: string = "Characters/Aatrox/Skins/Skin0/Materials/Aatrox_VFXBase_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Characters/Aatrox/Skins/Base/Aatrox_Base_TX_CM.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_R_body_mask.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Gradient_Texture"
                textureName: string = "ASSETS/Shared/Materials/Gradient_test_01.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Dissolve_SmoothStep"
                value: vec4 = { 0, 0.150000006, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dissolve_Bias"
                value: vec4 = { -0.200000003, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Pulse_Rate"
                value: vec4 = { 3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Pulse_Max"
                value: vec4 = { 0.400000006, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Gradient_Sharpness"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Sharpness"
                value: vec4 = { 0.00100000005, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 10, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Pulse_Offset"
                value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha"
                value: vec4 = { 1, 0, 0, 0 }
            }
        }
        shaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/SkinnedMesh/Aatrox_VFXBase"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        childTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                name: string = "transition"
                parentName: string = "normal"
                shaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "Dissolve_Bias"
                    driver: pointer = MaxMaterialDriver {
                        mDrivers: list[pointer] = {
                            FloatGraphMaterialDriver {
                                driver: pointer = LerpMaterialDriver {
                                    mBoolDriver: pointer = IsDeadDynamicMaterialBoolDriver {}
                                    mTurnOnTimeSec: f32 = 4
                                    mTurnOffTimeSec: f32 = 0
                                }
                                graph: embed = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0.00171930937
                                        0.216738746
                                        0.766768217
                                        1.00488436
                                    }
                                    values: list[f32] = {
                                        -0.22144419
                                        0.260138661
                                        0.752247512
                                        0.86541003
                                    }
                                }
                            }
                            FloatGraphMaterialDriver {
                                driver: pointer = LerpMaterialDriver {
                                    mBoolDriver: pointer = IsAnimationPlayingDynamicMaterialBoolDriver {
                                        mAnimationNames: list[hash] = {
                                            "Passive_Death"
                                        }
                                    }
                                    mTurnOnTimeSec: f32 = 3
                                }
                                graph: embed = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0.00321787666
                                        0.381477386
                                        0.997775316
                                    }
                                    values: list[f32] = {
                                        -0.225780264
                                        0.583815038
                                        0.994219661
                                    }
                                }
                            }
                        }
                    }
                }
                DynamicMaterialParameterDef {
                    name: string = "Pulse_Rate"
                    driver: pointer = LerpMaterialDriver {
                        mBoolDriver: pointer = HasBuffDynamicMaterialBoolDriver {
                            mScriptName: string = "AatroxR"
                        }
                        mOnValue: f32 = 5
                        mTurnOnTimeSec: f32 = 0
                        mTurnOffTimeSec: f32 = 0
                    }
                }
            }
        }
    }
    "Characters/Aatrox/Skins/Skin0/Materials/Wing_inst" = StaticMaterialDef {
        name: string = "Characters/Aatrox/Skins/Skin0/Materials/Wing_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Characters/Aatrox/Skins/Base/Aatrox_Wings_TX_CM.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_R_wing_mask.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Gradient_Texture"
                textureName: string = "ASSETS/Characters/Aatrox/Skins/Base/Particles/Aatrox_Base_R_mat_gradient.dds"
                addressU: u32 = 1
                addressV: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Mask_Intensity"
                value: vec4 = { 0.939999998, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scrolling_Scale"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scrolling_Rate"
                value: vec4 = { -0.5, -0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color"
                value: vec4 = { 1, 0.250980407, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dissolve_Bias"
                value: vec4 = { 0.785000026, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dissolve_SmoothStep"
                value: vec4 = { 0, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Gradient_Sharpness"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Sharpness"
                value: vec4 = { 0.00100000005, 0, 0, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_COLORDODGE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_ADDATIVE"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_LERP"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_DISSOLVE"
            }
        }
        shaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/SkinnedMesh/Scrolling_ColorDodge_Masked"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        childTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                name: string = "transition"
                parentName: string = "normal"
                shaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "Dissolve_Bias"
                    driver: pointer = SwitchMaterialDriver {
                        mElements: list[embed] = {
                            SwitchMaterialDriverElement {
                                mCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                                    mScriptName: string = "AatroxRFX"
                                }
                                mValue: pointer = LerpMaterialDriver {
                                    mBoolDriver: pointer = HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "AatroxRFX"
                                        mDeactivateEarlySeconds: f32 = 1
                                    }
                                    mOnValue: f32 = -1
                                    mOffValue: f32 = 1
                                    mTurnOnTimeSec: f32 = 2
                                }
                            }
                            SwitchMaterialDriverElement {
                                mCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                                    mScriptName: string = "AatroxRReviveMaterialOverride"
                                }
                                mValue: pointer = LerpMaterialDriver {
                                    mBoolDriver: pointer = HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "AatroxRReviveMaterialOverride"
                                    }
                                    mOffValue: f32 = -0.180000007
                                    mTurnOnTimeSec: f32 = 6
                                    mTurnOffTimeSec: f32 = 0
                                }
                            }
                            SwitchMaterialDriverElement {
                                mCondition: pointer = IsAnimationPlayingDynamicMaterialBoolDriver {
                                    mAnimationNames: list[hash] = {
                                        0x909068b6
                                    }
                                }
                                mValue: pointer = LerpMaterialDriver {
                                    mBoolDriver: pointer = IsAnimationPlayingDynamicMaterialBoolDriver {
                                        mAnimationNames: list[hash] = {
                                            0x909068b6
                                        }
                                    }
                                    mOnValue: f32 = -1
                                    mOffValue: f32 = 1
                                    mTurnOnTimeSec: f32 = 0.200000003
                                    mTurnOffTimeSec: f32 = 0.200000003
                                }
                            }
                            SwitchMaterialDriverElement {
                                mCondition: pointer = IsAnimationPlayingDynamicMaterialBoolDriver {
                                    mAnimationNames: list[hash] = {
                                        "taunt"
                                    }
                                }
                                mValue: pointer = LerpMaterialDriver {
                                    mBoolDriver: pointer = IsAnimationPlayingDynamicMaterialBoolDriver {
                                        mAnimationNames: list[hash] = {
                                            "taunt"
                                        }
                                    }
                                    mOnValue: f32 = -1
                                    mOffValue: f32 = 1
                                    mTurnOnTimeSec: f32 = 0.200000003
                                    mTurnOffTimeSec: f32 = 0.200000003
                                }
                            }
                        }
                        mDefaultValue: pointer = FloatLiteralMaterialDriver {
                            mValue: f32 = 1
                        }
                    }
                }
            }
        }
    }
    "Characters/Aatrox/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Aatrox_Q_Indicator_01" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Indicator_01"
            0x4c250437 = "Characters/Kayn/Skins/Skin0/Particles/Kayn_Base_Primary_R_tar_child"
            "Aatrox_Q_cas1" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_cas1"
            "Aatrox_Q_cas3" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_cas3"
            "Aatrox_Q_cas2" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_cas2"
            "Aatrox_AA_Trail_01" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_AA_Trail_01"
            "Aatrox_AA_Trail_03" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_AA_Trail_03"
            "Aatrox_AA_Trail_02" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_AA_Trail_02"
            0x57532b4b = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_AA_Hit_Tar01"
            0x58532cde = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_AA_Hit_Tar02"
            "Aatrox_W_mis" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_mis"
            "Aatrox_W_Beam_Tar" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Beam_Tar"
            "Aatrox_W_Core" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Core"
            "Aatrox_Q_Indicator_02" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Indicator_02"
            "Aatrox_Q_Indicator_03" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Indicator_03"
            "Aatrox_E_Dash" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Dash"
            "Aatrox_E_Active_buff" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Active_buff"
            "Aatrox_Q_Trail_01" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Trail_01"
            "Aatrox_Q_Trail_02" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Trail_02"
            "Aatrox_Q_Trail_03" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Trail_03"
            "Aatrox_Q_Indicator_01_Ally" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Indicator_01_Ally"
            "Aatrox_Q_Indicator_02_Ally" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Indicator_02_Ally"
            "Aatrox_Q_Indicator_03_Ally" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Indicator_03_Ally"
            "Aatrox_P_Ready" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_P_Ready"
            "Aatrox_R_Fear" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_R_Fear"
            "Aatrox_P_Activate" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_P_Activate"
            "Aatrox_E_Heal" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Heal"
            "Aatrox_Death_ambers" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Death_ambers"
            "Aatrox_R_Attack_01" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_R_Attack_01"
            "Aatrox_P_Hit_Tar" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_P_Hit_Tar"
            "Aatrox_R_Attack_02" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_R_Attack_02"
            "Aatrox_W_Cas" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Cas"
            "Aatrox_E_Dash_trail" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Dash_trail"
            "Aatrox_E_Dash2" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_E_Dash2"
            "Aatrox_W_Hand_glow_cas" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Hand_glow_cas"
            "Aatrox_Q_Hit_Tar" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Hit_Tar"
            "Aatrox_Q_Sweet_hit_tar" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Q_Sweet_hit_tar"
            "Aatrox_W_Core_Area" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Core_Area"
            "Aatrox_P_Attack_trail" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_P_Attack_trail"
            "Aatrox_R_Revive_end" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_R_Revive_end"
            "Aatrox_E_Buf_Sword" = 0x00000000
            "Aatrox_Passive_Sheathe_Sword" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Passive_Sheathe_Sword"
            "Aatrox_R_Revive_Duration" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_R_Revive_Duration"
            "Aatrox_R_Revive_Diration_Sword" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_R_Revive_Diration_Sword"
            "Aatrox_R_SpeedBuff" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_R_SpeedBuff"
            "Aatrox_P_Debuff" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_P_Debuff"
            "Aatrox_Recall_Ground" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Ground"
            "Aatrox_Recall_Beam" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Beam"
            "Aatrox_Recall_Weapon_glow" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Weapon_glow"
            "Aatrox_Recall_Hand_glow" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Recall_Hand_glow"
            "Aatrox_W_Core_End" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Core_End"
            "Aatrox_W_Beam_Tar_Break" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Beam_Tar_Break"
            "Aatrox_W_Hit_Tar" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Hit_Tar"
            "Aatrox_W_Beam_Tar_Pull" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_W_Beam_Tar_Pull"
            "Aatrox_AA_Crit_Hit_Tar" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_AA_Crit_Hit_Tar"
            "Aatrox_AA_Crit_Trail" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_AA_Crit_Trail"
            "Aatrox_Dance_Ground" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Dance_Ground"
            "Aatrox_Taunt_Ground" = "Characters/Aatrox/Skins/Skin0/Particles/Aatrox_Base_Taunt_Ground"
            0x5b2b3b83 = "Maps/Particles/SRX/Base/SRX_Audio_Hextech_Storm_loop"
            0x2c43403d = "Maps/Particles/SR/SRU_Braziers_Chemtech_Child_02"
            0x20bae730 = "Maps/Shipping/Map22/Particles/Set9/TFT9_Trait_Demacia_Celebration_Child7"
        }
    }
}
